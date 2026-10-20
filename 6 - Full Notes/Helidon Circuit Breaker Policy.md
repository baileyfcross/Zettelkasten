2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Circuit Breaker Policy

Helidon's `@CircuitBreaker` policy prevents repeated execution of logic that is likely to fail. It classifies failure and skipped exception types, evaluates failures over a configured request-volume window, and opens when the failure ratio reaches its threshold.

The policy also specifies how long an open breaker waits before trial execution and how many successful trials are required for recovery. It is the MicroProfile annotation-based realization of the general [[Circuit Breaker]] pattern.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
