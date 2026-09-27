2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core Change Tracking and Persistence

An EF Core context tracks the state of entity instances as unchanged, added, modified, or deleted. Property changes and relationship changes become a set of database commands when `SaveChanges` or its asynchronous counterpart is called.

Tracking supports convenient unit-of-work behavior, but it consumes memory and can preserve stale state in a long-lived context. Read-only queries can disable tracking when entity updates are not needed.

Entity Framework tracks materialized entities so changes can later be translated into insert, update, or delete commands when `SaveChanges` or its asynchronous form executes. Tracking connects object mutation to persistence but also creates a defined context lifetime and state boundary.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
