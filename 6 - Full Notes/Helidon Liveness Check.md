2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Liveness Check

A Helidon liveness check reports whether the runtime environment is sufficient for the microservice to perform its task at that moment. A liveness result of `DOWN` means the instance should be stopped and replaced rather than expected to recover to `UP` by itself.

A custom check uses `@Liveness` and can implement the health-check contract. The book's example compares heap use with maximum heap capacity and reports `UP` only while usage remains below its chosen threshold.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
