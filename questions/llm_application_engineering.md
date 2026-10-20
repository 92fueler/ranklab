# LLM application engineering

## Core questions

1. When would you use retrieval-augmented generation rather than fine-tuning,
   or combine them? Compare knowledge freshness, behavior, evaluation, latency,
   and maintenance.
2. How would you handle input exceeding a model's context limit? Explain which
   information must remain available and how you detect lost meaning.
3. How would an application preserve useful state across stateless model
   calls? Define what is stored, when it changes, and how it is retrieved.
4. How would you isolate untrusted retrieved text, tool results, and user
   content from instructions and tool authority? Define the prompt-injection
   threat model; do not assume a prompt alone guarantees protection.

No particular model, retrieval stack, state store, or context-management
technique is required.

## Additional engineering follow-ups

These are extensions, not hidden requirements:

- How do document updates and deletions affect retrieval freshness?
- How would you detect a summary that omits or distorts a critical constraint?
- What happens when concurrent requests update the same conversation state?
- Which permissions and approval boundaries limit damage if the model follows
  an injected instruction?
- How would you evaluate each proposal using representative failure cases?

## Related exercise

- [Local model evaluation](../ai_projects/local_model_evaluation.md) focuses on reproducible measurements.
