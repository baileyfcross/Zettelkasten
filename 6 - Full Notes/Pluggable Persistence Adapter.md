2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Pluggable Persistence Adapter

A pluggable persistence adapter implements a stable repository port for a particular storage technology. The book uses the same generic repository boundary and core product model while Spring supplies PostgreSQL and MongoDB adapters from different dependencies and configuration.

Pluggability requires keeping database annotations, identifiers, and mapping concerns from contaminating the reusable domain object. Adapter-specific representation can be separated when the two stores impose incompatible persistence details.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

