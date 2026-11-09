2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Declarative Transaction Boundary

Spring's `@Transactional` annotation defines a transaction around a managed method. The framework begins the transaction before invocation, commits after normal completion, and rolls it back for an unchecked exception or error under the default policy.

The boundary belongs around one business operation whose writes must succeed or fail together, such as creating a customer with its company and address. Isolation can be raised when concurrent operations would otherwise produce anomalies, but stronger isolation reduces concurrency. Because interception occurs through a Spring proxy, the location and call path of the annotated method are part of whether the boundary is actually applied.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
