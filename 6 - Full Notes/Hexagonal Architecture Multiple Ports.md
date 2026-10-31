2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Hexagonal Architecture Multiple Ports

The hexagon in hexagonal architecture symbolizes that an application can have several entry and exit points rather than only one user-interface side and one database side. REST and GraphQL may be separate driving ports, while a database, message queue, and remote API may be separate driven ports.

The number six is not a structural requirement. The polygon emphasizes symmetry among boundary mechanisms: each external technology reaches the core through a contract instead of receiving privileged access to the business logic.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

