2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Security Context

A Helidon security context carries the subject established for a server request. A handler can retrieve it from the request context and inspect the authenticated user, roles, and credentials, falling back to Helidon's anonymous subject when no user identity is present.

The context is the application-facing result of provider authentication and path authorization. It lets a response identify the current principal without making the handler repeat HTTP Basic parsing or provider-specific validation.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
