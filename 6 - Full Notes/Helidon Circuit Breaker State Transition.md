2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Circuit Breaker State Transition

A Helidon circuit breaker runs normally while closed, blocks execution while open, and permits trial invocations while half-open. After the configured delay, an open breaker enters half-open so it can test whether the protected operation has recovered.

Enough consecutive successful trials close the breaker, while a failure during half-open immediately opens it again. The request-volume threshold and failure ratio determine the earlier closed-to-open transition.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
