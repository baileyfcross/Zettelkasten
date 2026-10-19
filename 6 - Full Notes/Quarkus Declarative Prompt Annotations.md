2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Quarkus Declarative Prompt Annotations

Quarkus LangChain4j prompt annotations attach system and user instructions to methods in an AI service interface. Method parameters can be interpolated into the annotated prompt, making the prompt template part of the Java service contract rather than ad hoc controller text.

Keeping prompts near their typed entry points improves discoverability, but annotations are still executable application behavior. Their wording, variables, model settings, and expected outputs should be versioned and tested together.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
