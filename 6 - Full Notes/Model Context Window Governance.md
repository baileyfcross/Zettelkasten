2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Data and Model Design]] [[Prompt-Controlled Generative AI Applications]]

# Model Context Window Governance

Model context window governance treats the amount of input a model can process as both a capability and a data-exposure decision. A large window can preserve a complete document or conversation, while a small window requires splitting material and managing continuity across requests.

Sending more context simplifies some tasks but can expose more sensitive information and increase token cost. Fragmenting data limits each request's scope but can separate facts that must be interpreted together. The application should choose retrieval, chunking, and retention behavior according to task coherence, confidentiality, auditability, and the model's actual limits.

Operational sessions can control growth through prompt compression, pruning of obsolete or irrelevant evidence, and compaction of long investigations into structured summaries. Token telemetry should show both spend and proximity to the context limit because exceeding that limit can cause forgetting and unreliable incident reasoning.

The 2024 Java API source frames the context limit as a budget shared by the input messages and generated output. Long Slack histories, podcast transcripts, and reconstructed conversations must be measured before they are sent, and the requested maximum output must leave room within the selected model's limit. Choosing a larger-window model can avoid immediate splitting but also changes model selection and usage tradeoffs.

The current source applies that constraint to RAG and conversation history. Long documents are split before embedding, only top-ranked chunks are supplied to a question, and prior messages are explicitly reconstructed for a new turn. Advanced retrieval can rewrite the query and compress or summarize results, but those operations must preserve the evidence and conversational facts that the final response depends on.

# References

[[microsoftfoundryinaction.pdf]]

[[observabilityintheai-nativeera.pdf]]
[[chatgptforjava.epub]]
[[masteringspringai.epub]]
