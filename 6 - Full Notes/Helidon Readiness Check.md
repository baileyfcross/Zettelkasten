2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Readiness Check

A Helidon readiness check reports whether a microservice can currently perform its task. A `DOWN` readiness result can later return to `UP` without restarting the process, so it represents temporary ability to accept work rather than fatal runtime failure.

A custom procedure is marked with `@Readiness`. The example compares a required JVM-name property and returns a named `up` or `down` response, which appears under `/health/ready`.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
