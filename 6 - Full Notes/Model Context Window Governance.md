2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Data and Model Design]]

# Model Context Window Governance

Model context window governance treats the amount of input a model can process as both a capability and a data-exposure decision. A large window can preserve a complete document or conversation, while a small window requires splitting material and managing continuity across requests.

Sending more context simplifies some tasks but can expose more sensitive information and increase token cost. Fragmenting data limits each request's scope but can separate facts that must be interpreted together. The application should choose retrieval, chunking, and retention behavior according to task coherence, confidentiality, auditability, and the model's actual limits.

# References

[[microsoftfoundryinaction.pdf]]
