2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Metric Registry

A Helidon metric registry collects metrics and their metadata for one scope. Its API registers, creates, and retrieves measurements so application code can update a known metric without depending on the endpoint that will later expose it.

A CDI bean can inject `MetricRegistry`, optionally qualified by a registry scope, or code can obtain one from `RegistryFactory`. Injection requires a managed bean because the container supplies the registry reference.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
