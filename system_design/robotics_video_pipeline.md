# Figure AI – Multimodal training-data ingestion (candidate report)

## References

- [Public Figure candidate report](https://www.screna.ai/experience/aad0d809-9cc7-4e7b-aec2-48d6fa49b5cb).
- [Official Helix data-infrastructure role](https://job-boards.greenhouse.io/figureai/jobs/4345915006?gh_src=aijobsdesk): domain context, not an interview specification.

## Evidence status

The public candidate report describes collecting, filtering, and storing training uploads containing images, video, action sequences, labels, and metadata, including attention to collection bias. It is a candidate recollection, not a verified company rubric. The page's separately labeled AI-generated hints are not reported requirements. The official role corroborates robot-data infrastructure work, not this exact interview prompt. Additional requirements below are explicitly proposed practice assumptions.

## Problem statement

Design a backend that receives multimodal training data from many clients and makes usable collections available to training-data consumers. Clarify client types and collection workflows rather than assuming every upload comes directly from a robot.

## Functional requirements

Source-supported core:

- Receive media, action sequences, labels, and associated metadata.
- Filter and retain training data.
- Identify and address bias or coverage gaps in collected data.

Proposed exercise expansion:

- Show whether a submission is complete, usable, rejected, or awaiting processing.
- Preserve the association between media, actions, and labels.
- Handle corrections and repeated submissions with defined outcomes.
- Let authorized consumers find and retrieve selected collections.
- Explain quality exclusions and the basis of coverage assessments.

## Non-functional requirements

Set assumed targets for upload volume, object sizes, processing delay, retention, and consumer throughput. Clarify intermittent connectivity, acceptable loss, recovery time, access boundaries, and operating cost. Specify what evidence would justify a claim about collection bias; no universal threshold or fixed fleet size is reported.

## Optional failure conditions

A large upload stops halfway; labels arrive late; action timing is inconsistent with video; filtering disproportionately removes a useful scenario; a corrected source invalidates previously selected data. Define required behavior while leaving storage and processing choices open.
