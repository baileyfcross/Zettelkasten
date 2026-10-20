2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon Typed Response Entity

Helidon WebClient can decode a response entity directly into a requested Java type. A caller may request a `String` for raw text or a `JsonObject` when installed media support can map the response representation.

The convenience method combines request execution with entity conversion, while the lower-level response form remains available when code must inspect status or stream content. Choosing the form makes resource ownership explicit because a response opened directly is closed by the caller.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
