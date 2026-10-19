2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Quarkus AI Tool Registration

Quarkus LangChain4j requires tool-bearing beans to be explicitly associated with the AI service that may invoke them. The source shows this registration as the connection between a declarative service and Java methods exposed as model-selectable operations.

Explicit registration limits accidental capability exposure and makes the service's tool surface reviewable. It does not replace validation or authorization inside a tool, because model selection of a registered method is only a request to execute trusted application code.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
