2026-10-18 23:53

Status: #baby

Tags: [[Java RAG and Conversational Context]]

# RAG Context Window Budget

A RAG context window budget allocates limited model input space among system instructions, conversation history, the current question, retrieved passages, and room for the answer. Retrieval count cannot grow independently of these other consumers.

The source emphasizes context length as a practical constraint on retrieval design. Applications should bound and rank supplied passages, account for tokenization, and test whether added context improves grounding instead of assuming that more retrieved text always yields a better response.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
