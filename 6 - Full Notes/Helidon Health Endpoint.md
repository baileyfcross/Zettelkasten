2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Health Endpoint

Helidon exposes aggregate health at `/health` and type-specific results at `/health/live`, `/health/ready`, and `/health/started`. Each specialized endpoint executes only the checks belonging to its liveness, readiness, or startup category.

The JSON response contains an overall `UP` or `DOWN` status and a list of executed checks, each with its name, status, and optional data. An application with no custom checks can still return an empty check list with overall status `UP`.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
