2026-09-28 21:33

Status: #baby

Tags: [[Scientific Workflow Provenance]]

# Database State Provenance

Database state provenance identifies the version or transaction-time state of a mutable external database used by a computation. Recording only a query is insufficient when the same query can return different rows after the database changes.

A reproducible record therefore needs a snapshot, version identifier, or restoration mechanism that can recover the relevant state. This extends provenance beyond files and code to changing services. It serves the same purpose as [[Content-Addressed Research Data]]: distinguishing the actual input from a location or name that may later refer to something else.

# References

[[implementingreproducableresearch.pdf]]
