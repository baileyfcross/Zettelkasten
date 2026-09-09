2026-09-08 22:09

Status: #baby

Tags: [[Azure Cosmos DB Applications]]

# Cosmos DB Multi-Region Writes

Cosmos DB multi-region writes allow data changes to be accepted in more than one configured geographic region. This can reduce write latency for a globally distributed application whose users are far from a single primary location.

Writing in several places introduces coordination and cost beyond read-only replication. The 2019 portal exposes the option alongside geo-redundancy, making write geography an explicit database capability rather than an application-side failover script.

# References

[[c8andnetcore30projectsusingazure.pdf]]
