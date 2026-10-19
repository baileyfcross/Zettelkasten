2026-10-18 23:53

Status: #baby

Tags: [[Java LLM Framework Integration]]

# Spring AI Portable Model API

Spring AI exposes common Java interfaces over supported model providers so application code can depend on chat, embedding, image, and related model capabilities without directly constructing each vendor's wire protocol. Provider starters and configuration select the concrete implementation.

The abstraction supports replacement and comparison, but it does not erase capability differences. An application must test provider-specific model identifiers, option ranges, multimodal formats, tool support, safety behavior, and response metadata before treating two implementations as interchangeable.

# References

[[generativeai-drivenapplicationdevelopmentwithjava.epub]]
