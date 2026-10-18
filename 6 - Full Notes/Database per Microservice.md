2026-10-18 15:54

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Database per Microservice

Database per microservice gives each service a private persistence boundary that other services cannot access directly. The database may be a separate physical system or a separately controlled schema, but its structure and migrations belong to the service that owns the capability.

This pattern supports [[Independent Microservice Deployment]] and permits [[Polyglot Persistence]] because one service can change its storage without requiring every consumer to change. It also removes easy cross-service joins and transactions. Data needed elsewhere must move through contracts, messages, or local projections, and operations spanning owners need explicit consistency and recovery behavior. The pattern therefore enforces autonomy while exposing the real cost of distributed data rather than making that cost disappear.

# References

[[artofdecodingmicroservices.epub]]
