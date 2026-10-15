"""Offline SDK/transport checks; no real credentials or network access needed."""

import importlib
import json
import math
import os
from pathlib import Path
import socket
import tempfile
from types import SimpleNamespace as Obj
import unittest
from unittest.mock import patch

import httpx
import requests
import turbopuffer
import voyageai
import yaml

from ranklab.candidates import get_attr
from ranklab.cases import load_case
from ranklab.evaluation import evaluate, submit
from ranklab.reranking import rerank_pairs
from ranklab.retrieval import ann_query, embed_query
from ranklab.settings import required_env

ENV = {
    "VOYAGE_API_KEY": "test-key", "VOYAGE_MODEL": "voyage-3",
    "VOYAGE_RERANK_MODEL": "rerank-2", "TURBOPUFFER_API_KEY": "test-key",
    "TPUF_REGION": "aws-us-west-2", "TPUF_NAMESPACE": "test-index",
    "EVAL_AUTH_EMAIL": "test@example.test",
    "EVAL_ENDPOINT": "https://evaluation.example.test/evaluate",
    "GRADE_ENDPOINT": "https://evaluation.example.test/grade",
}
IDS = [f"candidate-{i}" for i in range(10)]


def embedding_response(vectors):
    return Obj(data=[Obj(embedding=vector) for vector in vectors], usage=Obj(total_tokens=3))


def reranking_response(pairs):
    return Obj(data=[Obj(index=index, relevance_score=score) for index, score in pairs],
               usage=Obj(total_tokens=3))


class BasicsTests(unittest.TestCase):
    def setUp(self):
        self.enterContext(patch.dict(os.environ, ENV, clear=True))
        self.enterContext(patch.object(socket.socket, "connect",
                                      side_effect=AssertionError("Unexpected network access")))

    def case_file(self, value):
        folder = Path(self.enterContext(tempfile.TemporaryDirectory()))
        path = folder / "case.yml"
        path.write_text(yaml.safe_dump(value), encoding="utf-8")
        return path

    def test_import_without_credentials(self):
        with patch.dict(os.environ, {}, clear=True):
            for name in ("settings", "cases", "candidates", "retrieval", "reranking", "evaluation"):
                importlib.reload(importlib.import_module(f"ranklab.{name}"))

    def test_missing_and_placeholder_settings(self):
        for value in ("", "  ", "YOUR_API_KEY", "REDACTED_CREDENTIAL", "https://EXAMPLE.INVALID"):
            with self.subTest(value=value), patch.dict(os.environ, {"VALUE": value}):
                with self.assertRaises(ValueError):
                    required_env("VALUE")

    def test_raw_case_naming_styles(self):
        # Generic fixtures keep tests independent of private reference folders.
        raw = {"title": "Example role", "natural_language_description": "Example description",
               "hard_criteria": ["Required qualification"], "soft_criteria": ["Preferred skill"]}
        for style in (lambda key: key, lambda key: key.title(),
                      lambda key: key.replace("_", " ").title()):
            with self.subTest(style=style):
                fixture = {style(key): value for key, value in raw.items()}
                self.assertEqual(load_case(self.case_file(fixture)), raw)

    def test_case_defaults_and_preserves_text(self):
        case = {"title": "Role", "natural_language_description": "  Exact wording  ",
                "hard_criteria": ["Must have X"]}
        loaded = load_case(self.case_file(case))
        self.assertEqual(loaded["natural_language_description"], case["natural_language_description"])
        self.assertEqual(loaded["soft_criteria"], [])

    def test_invalid_case_shapes(self):
        valid = {"title": "Role", "natural_language_description": "Description", "hard_criteria": []}
        for case in (None, [], {**valid, "hard_criteria": "Not a list"},
                     {**valid, "title": ""}, {**valid, "soft_criteria": [None]},
                     {**valid, "Title": "Duplicate"}):
            with self.subTest(case=case), self.assertRaises(ValueError):
                load_case(self.case_file(case))

    def test_candidate_dict_and_nested_access(self):
        self.assertEqual(get_attr({"items": "field"}, "items"), "field")
        self.assertEqual(get_attr({"attributes": {"summary": "nested"}}, "summary"), "nested")
        self.assertEqual(get_attr(Obj(attributes={"summary": "nested"}), "summary"), "nested")
        self.assertEqual(get_attr({}, "missing", "unknown"), "unknown")
        self.assertIsNone(get_attr({"summary": None}, "summary", "unknown"))

    def test_real_embedding_sdk_serialization(self):
        with patch.object(voyageai.Embedding, "create", return_value=embedding_response([[0.1, 0.2]])) as create:
            self.assertEqual(embed_query("query text"), [0.1, 0.2])
        self.assertEqual(create.call_args.kwargs["input"], ["query text"])
        self.assertEqual(create.call_args.kwargs["input_type"], "query")
        self.assertEqual(create.call_args.kwargs["model"], "voyage-3")

    def test_invalid_embedding_responses(self):
        for vectors in ([], [[], []], [[]], [[math.nan]], [[math.inf]], [[0.0, 0.0]]):
            with self.subTest(vectors=vectors), patch.object(
                voyageai.Embedding, "create", return_value=embedding_response(vectors)
            ), self.assertRaises(ValueError):
                embed_query("query")

    def test_invalid_query_inputs(self):
        for query in ("", "   ", None, ["query"]):
            with self.subTest(query=query), self.assertRaises(ValueError):
                embed_query(query)

    def test_real_ann_sdk_http_transport_and_rows(self):
        observed = []
        def handler(request):
            observed.append(request)
            return httpx.Response(200, json={"rows": [{"id": "candidate-1", "$dist": 0.25,
                                                       "rerankSummary": "A profile"}]})
        client = turbopuffer.Turbopuffer(api_key="test-key", region=ENV["TPUF_REGION"],
                    http_client=httpx.Client(transport=httpx.MockTransport(handler)), max_retries=0)
        with patch.object(turbopuffer, "Turbopuffer", return_value=client):
            result = ann_query([0.1, 0.2], top_k=20)
        self.assertTrue(client.is_closed())
        payload = json.loads(observed[0].content)
        self.assertEqual(payload["rank_by"], ["vector", "ANN", [0.1, 0.2]])
        self.assertEqual(payload["top_k"], 20)
        self.assertTrue(payload["include_attributes"])
        self.assertEqual(get_attr(result.rows[0], "rerankSummary"), "A profile")
        self.assertEqual(get_attr(result.rows[0], "$dist"), 0.25)

    def test_invalid_ann_arguments_before_network(self):
        for vector, k in (([], 10), ([0, 0], 10), ([math.inf], 10), ([0.1], 0),
                          ([0.1], True), ([0.1], 10001)):
            with self.subTest(vector=vector, k=k), self.assertRaises(ValueError):
                ann_query(vector, k)

    def test_real_reranker_sdk_alignment(self):
        with patch.object(voyageai.Reranking, "create",
                          return_value=reranking_response([(1, 0.9), (0, 0.2)])):
            self.assertEqual(rerank_pairs("query", ["first", "second"]), [0.2, 0.9])

    def test_incomplete_or_duplicate_reranking_is_an_error(self):
        for pairs in ([(0, 0.5)], [(0, 0.5), (0, 0.4)], [(0, math.nan), (1, 0.5)]):
            with self.subTest(pairs=pairs), patch.object(voyageai.Reranking, "create",
                return_value=reranking_response(pairs)), self.assertRaises(ValueError):
                rerank_pairs("query", ["first", "second"])

    def test_empty_reranking_needs_no_credentials(self):
        with patch.dict(os.environ, {}, clear=True):
            self.assertEqual(rerank_pairs("query", []), [])

    def test_evaluator_real_http_request_serialization(self):
        seen = []
        def respond(session, request, **kwargs):
            seen.append((request, kwargs))
            response = requests.Response()
            response.status_code = 200
            response._content = b'{"average_final_score": 80}'
            return response
        with patch.object(requests.Session, "send", new=respond):
            result = evaluate("cases/example.yml", IDS)
            submit({"example.yml": IDS})
        self.assertEqual(result["average_final_score"], 80)
        self.assertEqual(json.loads(seen[0][0].body), {"config_path": "example.yml", "object_ids": IDS})
        self.assertEqual(json.loads(seen[1][0].body), {"config_candidates": {"example.yml": IDS}})
        self.assertEqual(seen[0][0].headers["Authorization"], ENV["EVAL_AUTH_EMAIL"])
        self.assertEqual(seen[0][1]["timeout"], 60)

    def test_invalid_selection_rejected_before_request(self):
        for ids in ([], IDS[:9], IDS + ["extra"], ["same"] * 10, IDS[:9] + [None]):
            with self.subTest(ids=ids), self.assertRaises(ValueError):
                evaluate("case.yml", ids)
        with self.assertRaises(ValueError):
            submit({"directory/case.yml": IDS})
        with self.assertRaises(ValueError):
            submit({})

    def test_evaluation_http_and_json_errors_propagate(self):
        def respond(session, request, **kwargs):
            response = requests.Response()
            response.status_code = 503
            response._content = b'service unavailable'
            return response
        with patch.object(requests.Session, "send", new=respond), self.assertRaises(requests.HTTPError):
            evaluate("case.yml", IDS)
        def invalid_json(session, request, **kwargs):
            response = requests.Response()
            response.status_code = 200
            response._content = b'[]'
            return response
        with patch.object(requests.Session, "send", new=invalid_json), self.assertRaises(ValueError):
            evaluate("case.yml", IDS)

    def test_helpers_compose_into_an_offline_baseline(self):
        case = load_case(self.case_file({
            "title": "Example role", "natural_language_description": "Example description",
            "hard_criteria": ["Required qualification"], "soft_criteria": [],
        }))
        rows = [{"id": candidate_id, "rerankSummary": f"Profile {i}"}
                for i, candidate_id in enumerate(IDS)]
        http_client = httpx.Client(transport=httpx.MockTransport(
            lambda request: httpx.Response(200, json={"rows": rows})))
        client = turbopuffer.Turbopuffer(api_key="test-key", region=ENV["TPUF_REGION"],
                                        http_client=http_client, max_retries=0)
        with patch.object(voyageai.Embedding, "create", return_value=embedding_response([[0.1, 0.2]])), \
             patch.object(turbopuffer, "Turbopuffer", return_value=client), \
             patch.object(voyageai.Reranking, "create",
                          return_value=reranking_response([(i, i / 10) for i in reversed(range(10))])):
            embedding = embed_query(case["natural_language_description"])
            candidates = ann_query(embedding, 10).rows
            scores = rerank_pairs(case["natural_language_description"],
                                  [get_attr(row, "rerankSummary") for row in candidates])
        selected = [row.id for _, row in sorted(zip(scores, candidates), key=lambda x: x[0], reverse=True)]
        self.assertEqual(selected, list(reversed(IDS)))
        def respond(session, request, **kwargs):
            self.assertEqual(json.loads(request.body)["object_ids"], selected)
            response = requests.Response()
            response.status_code = 200
            response._content = b'{"ok": true}'
            return response
        with patch.object(requests.Session, "send", new=respond):
            self.assertEqual(evaluate("example.yml", selected), {"ok": True})


if __name__ == "__main__":
    unittest.main()
