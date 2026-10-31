2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Application Adapter

An application adapter implements or invokes a port by translating between an external technology and the application's contract. It supplies the promised behavior without requiring the client or core to know which concrete class or infrastructure provides it.

A REST controller can adapt HTTP and JSON into method calls, while a repository adapter can translate domain persistence operations into a database-specific API. Replacing one adapter should not require rewriting the business rules behind the port.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

