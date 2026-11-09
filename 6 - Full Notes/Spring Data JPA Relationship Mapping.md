2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Data JPA Relationship Mapping

Spring Data JPA repositories operate over Jakarta Persistence entities whose annotations describe identity and relationships. Entity, generated-value, many-to-one, one-to-many, and join-column metadata allow the persistence provider to coordinate object graphs and foreign keys rather than requiring every join and insert to be written by hand.

The owning side and transaction boundary still matter. A service may save a referenced company before a customer so its identifier is available, then persist addresses inside the same transaction. JPA is useful when relationship management and a persistence context justify its complexity; smaller aggregates may be more predictable with [[Spring Data JDBC Aggregate Mapping]].

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
