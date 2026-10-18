2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]] [[Prompt-Controlled Generative AI Applications]]

# Agent System Prompt as Behavioral Contract

An agent system prompt acts as a behavioral contract by stating the agent’s role, approved sources, tool-use rules, response format, refusal conditions, and escalation expectations. It gives the model a stable operating boundary that is more precise than a generic request to be helpful or accurate.

Like a contract, the prompt must be versioned, tested, and interpreted together with enforceable controls. It cannot grant permissions that the identity layer denies, nor reliably replace schema validation or safety filters. Evaluation should verify the behaviors it promises, especially source use, tool selection, uncertainty disclosure, and handling of unsupported requests.

Operational instruction files make the contract domain-specific by stating the situation, goal, and approach an agent should follow. Guidance such as starting with cheaper metrics, bounding the timeframe, and using a known investigation sequence can reduce exploratory queries without requiring a newly trained model.

The Java ChatGPT source demonstrates the contract with two Discord bots. A system message establishes the Q&A assistant's role and supplied knowledge boundary, while a separate moderation prompt defines locally unwanted solicitation. When the first Q&A instruction merely encouraged helpfulness, the model invented unsupported product features; changing it to remain within the provided FAQ and avoid assumptions materially improved the behavior.

# References

[[microsoftfoundryinaction.pdf]]

[[observabilityintheai-nativeera.pdf]]
[[chatgptforjava.epub]]
