2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Persistence Context and EntityManager

A Jakarta persistence context is the managed set of entity instances associated with a persistence unit. The EntityManager operates through that context to persist, find, merge, and remove entities, tracking the relationship between in-memory instances and database state.

In Jakarta EE, the EntityManager is a runtime-provided managed object rather than an object application code normally constructs. It is injected for a selected persistence unit, and state-changing operations run within transactions that the container can begin, join, and commit. Removing an entity first changes its managed state, with the database change coordinated through the context and transaction.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
