2026-09-08 22:09

Status: #baby

Tags: [[Azure Cosmos DB Applications]]

# MongoDB CRUD Operations

MongoDB CRUD operations create, read, update, and delete documents through a collection. The task tracker reads all work items with a filter, inserts new work-item documents, and uses their identifiers when acting on individual records.

The operations belong behind an application service or repository so controllers express user actions rather than driver details. Results still need error handling and validation because a compatible document API does not make external storage infallible.

# References

[[c8andnetcore30projectsusingazure.pdf]]
