2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Knowledge Base Retrieval Verification

Knowledge base retrieval verification checks that an agent actually consults the intended knowledge source and receives relevant evidence before answering. A configured connection alone does not prove that retrieval occurred, that the correct index was used, or that the returned passages support the final claim.

Verification can inspect traces, citations, retrieved chunks, query reformulation, and groundedness results for representative requests. Tests should include known-answer questions, missing-answer cases, and overlapping sources. This separates retrieval failure from generation failure and catches silent fallback to model memory when the governed knowledge path is unavailable.

# References

[[microsoftfoundryinaction.pdf]]
