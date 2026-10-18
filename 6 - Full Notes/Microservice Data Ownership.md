2026-10-18 15:54

Status: #baby

Tags: [[Microservice Boundaries and Data]]

# Microservice Data Ownership

Microservice data ownership gives one service authority over the data that implements its business capability. Other services ask through a published API or consume an event instead of reading or changing the owner's tables directly. This keeps persistence changes inside the owning boundary and prevents a shared schema from becoming an undeclared system-wide contract.

Ownership does not mean other services never retain related facts. A consumer may keep a local projection needed for its own work, but the source of authority and update path must remain clear. Duplication introduces staleness and reconciliation questions, while cross-service operations may require eventual consistency or compensation. [[Database per Microservice]] is a deployment mechanism for enforcing this principle, not the principle itself.

# References

[[artofdecodingmicroservices.epub]]
