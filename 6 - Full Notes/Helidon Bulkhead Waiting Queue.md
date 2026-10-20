2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Bulkhead Waiting Queue

The Helidon bulkhead waiting queue parks tasks that arrive after the concurrent-execution limit has been reached. Its configured capacity must be positive and applies only when the protected invocation is also annotated for asynchronous execution.

Without `@Asynchronous`, the waiting-queue parameter is not active. This ties queued admission to the execution model rather than treating the queue as a general buffer for every bulkhead-protected call.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
