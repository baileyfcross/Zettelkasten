2026-11-06 13:52

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# BASE Transaction

A BASE transaction divides one ideal system-wide atomic operation into smaller local transactions whose effects propagate asynchronously. Each local change can retain an ordinary atomic boundary, but messages create a delay between the first committed change and the last participating service's update.

This structure supports basic availability, soft intermediate state, and eventual consistency across partitions. It does not make correctness automatic: message loss can prevent convergence, while duplicate or reordered delivery can corrupt a non-idempotent operation. A design must state which temporary inconsistencies the business permits and supply persistence, retries, deduplication, or compensation accordingly. BASE and a local ACID transaction solve different scopes rather than replacing one another.

# References

[[practicalmicroservicesarchitecturalpatterns.epub]]
