2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Health Check Interface

The MicroProfile `HealthCheck` interface is the programmatic contract for a custom Helidon health procedure. Its methods include `call`, `name`, `path`, and `type`, allowing a class to evaluate state and identify how the result should be exposed.

The implementation class is placed in application scope and marked with the appropriate liveness, readiness, or startup annotation. Its `call()` method returns a [[Helidon Health Check Response]] each time the corresponding endpoint evaluates the procedure.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
