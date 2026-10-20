2026-10-19 22:48

Status: #baby

Tags: [[Helidon Fault Tolerance and Health]]

# Helidon Asynchronous Fault-Tolerance Invocation

Helidon's `@Asynchronous` annotation executes a managed invocation without blocking its calling thread. The annotated method must return `Future` or `CompletionStage` so the caller has an object representing eventual completion.

The policy is suited to I/O or long-running computation and has no annotation parameters. It also activates the waiting-queue behavior of [[Helidon Bulkhead Waiting Queue]] when the same invocation is protected by a bulkhead.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
