2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Spring AI Tool Callback

A Spring AI ToolCallback describes an operation that a model may request and connects that description to application-controlled execution. Its definition includes a tool name, purpose, input schema, and callback behavior so the model can construct arguments while Java code performs the action.

The callback is a trust boundary. Arguments require validation, failures need structured handling, and the executing identity must have only the permissions that the operation actually needs.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
