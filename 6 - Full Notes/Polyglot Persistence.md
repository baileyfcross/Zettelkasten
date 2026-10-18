2026-09-27 11:51

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]] [[Microservice Boundaries and Data]]

# Polyglot Persistence

Polyglot persistence uses different storage technologies for different data families according to their access and consistency needs. Relational data, distributed documents, cached values, files, and queued messages need not be forced into one engine.

Better local fit increases system-wide operational complexity. The architecture must define ownership, synchronization, backup, monitoring, and failure behavior across stores rather than assuming each data choice is independent.

In a microservice architecture, polyglot persistence is enabled by keeping each service's database private. One capability can select a relational store while another selects a document or in-memory store, but consumers should depend on the service contract rather than the chosen schema. This freedom increases the need for explicit data authority and consistency between service-owned copies.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
[[artofdecodingmicroservices.epub]]
