2026-09-05 16:28

Status: #baby

Tags: [[Language and Speech Generation]]

# Prompt Repository

A prompt repository is a managed collection of messages an assistant can present during known interaction states. Entries may include text, prerecorded audio, variants, and metadata about where each prompt applies.

Centralizing prompts supports consistent wording and easier revision. It also lets a [[Dialog Manager]] select among alternate messages instead of embedding user-facing language directly in transition logic.

Operational AI workflows extend this idea by storing system prompts in source control as versioned contracts. The prompt's required output structure and the deterministic validator that consumes it must change together.

# References

[[aiassistants.epub]]

[[agenticaifordevopsengineers.pdf]]
