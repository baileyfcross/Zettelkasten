2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core Transactions

A database transaction groups operations so they either succeed as a unit or are rolled back together. EF Core applies transactional behavior when saving a compatible group of changes and also permits explicit transaction control for broader workflows.

Transactions protect consistency, but long-running transactions hold resources and can increase contention. A transaction boundary should therefore contain the smallest coherent business operation and define how failures are surfaced or retried.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
