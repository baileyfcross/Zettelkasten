2026-10-18 16:07

Status: #baby

Tags: [[Java OpenAI API Integration]]

# Java Chat Request Model

A Java chat request model represents the JSON body sent to the book's 2024 chat-completions endpoint. Its required core is a model identifier and an ordered array of messages, each containing a role and content. Optional fields control tools, sampling, output length, stop sequences, streaming, response format, and other generation behavior.

Typed request classes make the wire contract visible and let a JSON library serialize it consistently. Because most fields are optional, the [[Builder Pattern]] can collect only the settings needed for one call while retaining defaults. The model should still validate documented ranges before sending the request; a convenient builder must not permit structurally valid Java objects that violate the endpoint contract.

# References

[[chatgptforjava.epub]]
