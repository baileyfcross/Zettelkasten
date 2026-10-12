2026-09-27 18:30

Status: #baby

Tags: [[Network Copilot Design]]

# Network Copilot Response Pipeline

A network copilot response pipeline receives a question, identifies intent, resolves device state, selects relevant knowledge, assembles a prompt, invokes the chosen model, and formats the answer. Making these stages explicit prevents “the copilot” from becoming one opaque model call.

Each stage can record its input and failure independently. The response should expose assumptions, context age, and recommended verification, especially when proposing commands. Evaluation of the complete pipeline matters more than model evaluation alone because stale knowledge or incorrect intent can defeat an otherwise capable model.

# References

[[ainetworkingcookbook.pdf]]
