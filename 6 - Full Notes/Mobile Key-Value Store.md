2026-09-22 23:04

Status: #baby

Tags: [[Mobile Data Synchronization and Notifications]]

# Mobile Key-Value Store

A mobile key-value store persists values under application-defined keys without requiring a relational schema. It is useful for cached blobs, preferences, tokens, and small records whose lookup identity is already known.

The book uses Akavache as an asynchronous .NET Standard implementation with memory, local-machine, and user-account-backed stores. A key-value cache simplifies retrieval, but it still needs expiration, serialization, and invalidation policies.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
