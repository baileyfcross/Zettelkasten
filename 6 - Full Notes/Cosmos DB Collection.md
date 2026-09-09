2026-09-08 22:09

Status: #baby

Tags: [[Azure Cosmos DB Applications]]

# Cosmos DB Collection

A Cosmos DB collection is the document container configured within the book's MongoDB-compatible database. It holds work-item documents and has capacity settings that affect storage limits and request throughput.

The 2019 portal distinguishes a fixed-capacity collection from an unlimited option that requires a partition key. The choice affects how data can grow and distribute, so collection design must consider identifiers and access patterns before production use.

# References

[[c8andnetcore30projectsusingazure.pdf]]
