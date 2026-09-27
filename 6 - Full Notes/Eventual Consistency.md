2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]] [[Event Sourcing and Projections]] [[Cloud Data Storage Selection and Consistency]]

# Eventual Consistency

Eventual consistency means that a read model may temporarily lag behind committed source changes but is expected to converge after updates propagate. In a split command-and-query system, a successful write can precede the corresponding read projection, so a user may briefly see the old value. The application must make that delay acceptable through workflow design, status reporting, or a stronger consistency path for operations that cannot tolerate stale reads.

In an event-sourced system, the event stream is updated before asynchronous [[Projection]]s consume the new event. The consistency delay is therefore the interval between appending the event and updating every affected [[Read Model]]. Reliable subscriptions, retries, and [[Projection Checkpoint]]s make convergence possible, while the interface must not promise immediate visibility it cannot provide.

Distributed document databases can expose eventual consistency as a selectable replication contract, improving availability or latency while requiring the application to tolerate temporarily stale reads.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-ondomain-drivendesignwithnetcore.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
