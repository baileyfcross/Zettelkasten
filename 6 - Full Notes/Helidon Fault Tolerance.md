2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Fault Tolerance

Helidon Fault Tolerance is Helidon MP's compatible implementation of MicroProfile Fault Tolerance. It applies annotations to managed business methods so service restarts, network delays, temporary infrastructure failures, slow execution, and excess concurrency can be handled by declared policies.

The available policies cover retry, timeout, circuit breaking, bulkheads, fallbacks, and asynchronous execution. Each addresses a different failure condition, and their parameters state when an invocation should be attempted, rejected, redirected, or allowed to continue.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
