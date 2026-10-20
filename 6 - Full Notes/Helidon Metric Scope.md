2026-10-19 22:48

Status: #baby

Tags: [[Helidon Metrics Instrumentation]]

# Helidon Metric Scope

Helidon supports a separate metric scope and registry for base, vendor, application, and custom measurements. Base scope represents operating-system or Java-runtime measurements, vendor scope contains implementation-provided indicators, and application scope contains measurements declared or registered by application code.

Each standard scope has a corresponding endpoint such as `/metrics/base`, `/metrics/vendor`, or `/metrics/application`. Custom metrics use application scope by default unless another scope is explicitly selected.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
