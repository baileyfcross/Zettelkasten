2026-10-18 16:07

Status: #baby

Tags: [[Prompt-Controlled Generative AI Applications]]

# Conversation History Reconstruction

Conversation history reconstruction sends the prior messages needed for a model to interpret the current turn. The source treats a stateless chat request as lacking memory unless the application includes relevant earlier user and assistant content in the ordered message array.

Reconstruction should be selective rather than an automatic copy of everything ever said. Older turns consume the [[Model Context Window Governance|context window]], raise token use, and may carry obsolete assumptions. The client therefore owns persistence, ordering, pruning, and any summary that replaces earlier detail. An assistant response becomes durable conversational state only when the application stores and supplies it again.

The current source implements this explicitly across a browser client and Spring service. The client sends an ordered list of prior user and assistant entries with the new question; the service converts those entries back into role-specific messages, adds retrieved system context when enabled, appends the current user message, and creates the prompt. This history exists only because the application transports and reconstructs it.

# References

[[chatgptforjava.epub]]
[[masteringspringai.epub]]
