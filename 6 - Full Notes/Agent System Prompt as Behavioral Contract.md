2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Agent System Prompt as Behavioral Contract

An agent system prompt acts as a behavioral contract by stating the agent’s role, approved sources, tool-use rules, response format, refusal conditions, and escalation expectations. It gives the model a stable operating boundary that is more precise than a generic request to be helpful or accurate.

Like a contract, the prompt must be versioned, tested, and interpreted together with enforceable controls. It cannot grant permissions that the identity layer denies, nor reliably replace schema validation or safety filters. Evaluation should verify the behaviors it promises, especially source use, tool selection, uncertainty disclosure, and handling of unsupported requests.

# References

[[microsoftfoundryinaction.pdf]]
