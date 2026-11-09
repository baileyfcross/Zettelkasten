2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Tools Agents and Protocols]]

# Spring AI Tool Callback

A Spring AI ToolCallback describes an operation that a model may request and connects that description to application-controlled execution. Its definition includes a tool name, purpose, input schema, and callback behavior so the model can construct arguments while Java code performs the action.

The callback is a trust boundary. Arguments require validation, failures need structured handling, and the executing identity must have only the permissions that the operation actually needs.

In the current source's Spring AI version, `FunctionCallbackWrapper` associates an injected Java `Function` with a model-visible name, description, and response converter. The facilities example registers separate callbacks for a local leasing API, web-scraped contact data, and an external weather API, illustrating why each callback requires its own credentials, availability assumptions, error handling, and output policy.

In the CRM assistant, a described Java function wraps a declarative HTTP client that finds a customer by email. Its input record and description tell the model what arguments the callback accepts and when the live-system lookup is appropriate. The callback output returns to the model for synthesis, so validation and authorization remain necessary at the tool boundary rather than being delegated to the prompt.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
