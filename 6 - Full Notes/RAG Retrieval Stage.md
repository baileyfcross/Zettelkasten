2026-09-30 17:53

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]] [[Microsoft Foundry Data and Model Design]]

# RAG Retrieval Stage

The RAG retrieval stage transforms a user query into a search representation, locates relevant indexed chunks, and ranks candidates for use as context. Vector similarity can be combined with keyword search, metadata filters, or reranking to improve relevance.

Retrieval must enforce the requesting user's access rights and return evidence with stable provenance. The stage narrows a large knowledge collection into a bounded context but does not guarantee that the selected material is sufficient or correct.

Microsoft Foundry can expose this stage to an agent as a knowledge-base retrieval tool. Agent instructions should require the tool before answering a knowledge-bound question, select the appropriate approved source for the topic, and treat an empty result as a reason to decline or escalate rather than as permission to answer from model memory.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[microsoftfoundryinaction.pdf]]
