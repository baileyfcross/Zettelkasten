2026-10-02 15:13

Status: #baby

Tags: [[Microsoft Foundry Enterprise Agent Integrations]]

# Agent Tool Routing Instruction

An agent tool routing instruction explains when a tool should be selected, which requests it supports, what arguments it expects, and when it should not be used. Precise descriptions matter because the model chooses among tools by interpreting their names, schemas, and instructions rather than by understanding the implementation behind them.

Routing guidance should distinguish overlapping tools and define how to handle ambiguity, missing inputs, and failures. It is then tested with examples that require each tool, no tool, or clarification. Better routing instructions reduce accidental calls, but authorization and schema validation must still constrain whatever selection the model makes.

# References

[[microsoftfoundryinaction.pdf]]
