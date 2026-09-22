2026-09-21 22:12

Status: #baby

Tags: [[CQRS and Ledger Data Architecture]]

# Eventual Consistency

Eventual consistency means that a read model may temporarily lag behind committed source changes but is expected to converge after updates propagate. In a split command-and-query system, a successful write can precede the corresponding read projection, so a user may briefly see the old value. The application must make that delay acceptable through workflow design, status reporting, or a stronger consistency path for operations that cannot tolerate stale reads.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

