2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Polyglot Persistence

Polyglot persistence uses different storage technologies for different data families according to their access and consistency needs. Relational data, distributed documents, cached values, files, and queued messages need not be forced into one engine.

Better local fit increases system-wide operational complexity. The architecture must define ownership, synchronization, backup, monitoring, and failure behavior across stores rather than assuming each data choice is independent.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
