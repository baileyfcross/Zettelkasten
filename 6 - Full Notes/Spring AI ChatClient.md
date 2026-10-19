2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Spring AI ChatClient

Spring AI ChatClient provides a fluent Java interface for assembling a prompt, supplying user or system content, invoking a configured chat model, and obtaining either the generated content or a richer response. The book uses it as the application-facing layer above provider-specific model clients.

The client can also participate in advisor chains, structured-output conversion, tools, observations, and retrieval. That makes it a composition point rather than merely an HTTP wrapper, so cross-cutting behavior should remain visible in configuration and tests.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
