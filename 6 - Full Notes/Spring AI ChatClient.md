2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Spring AI ChatClient

Spring AI ChatClient provides a fluent Java interface for assembling a prompt, supplying user or system content, invoking a configured chat model, and obtaining either the generated content or a richer response. The book uses it as the application-facing layer above provider-specific model clients.

The client can also participate in advisor chains, structured-output conversion, tools, observations, and retrieval. That makes it a composition point rather than merely an HTTP wrapper, so cross-cutting behavior should remain visible in configuration and tests.

In the source's Spring AI 0.8.1 API, a `Prompt` is a container for ordered message objects and `ChatClient.call` returns a response whose result contains the assistant content. The examples progress from a plain string call to role-separated prompts, templates, retrieval context, and conversation history, showing that the client boundary stays stable while the application deliberately assembles richer input.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
[[masteringspringai.epub]]
