2026-09-08 22:09

Status: #baby

Tags: [[Azure Cosmos DB Applications]] [[Cloud Data Storage Selection and Consistency]]

# Document Database

A document database stores records as self-describing documents rather than rows constrained to one relational table shape. Documents can contain the fields needed for an application object and are commonly addressed through a collection and a unique identifier.

The book presents Cosmos DB as the successor branding for Microsoft's DocumentDB service and accesses work-item documents through a MongoDB-compatible API. Document flexibility does not remove the need for deliberate identifiers, query patterns, and capacity planning.

Embedding related information in one document can reduce cross-record coordination, while relationships that require independent updates or broad joins may remain a better fit for another data model.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
