2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Spring AI Tool Callback

A Spring AI ToolCallback describes an operation that a model may request and connects that description to application-controlled execution. Its definition includes a tool name, purpose, input schema, and callback behavior so the model can construct arguments while Java code performs the action.

The callback is a trust boundary. Arguments require validation, failures need structured handling, and the executing identity must have only the permissions that the operation actually needs.

In the current source's Spring AI version, `FunctionCallbackWrapper` associates an injected Java `Function` with a model-visible name, description, and response converter. The facilities example registers separate callbacks for a local leasing API, web-scraped contact data, and an external weather API, illustrating why each callback requires its own credentials, availability assumptions, error handling, and output policy.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
