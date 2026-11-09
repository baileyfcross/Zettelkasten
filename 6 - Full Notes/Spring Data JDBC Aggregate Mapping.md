2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Data JDBC Aggregate Mapping

Spring Data JDBC maps a relational aggregate as a root and the objects owned by that root. Saving the root persists the aggregate together, and loading is eager rather than delegated to lazy proxies. There is no first-level persistence-context cache or automatic dirty checking, so reads and saves have comparatively direct behavior.

The model works well for small, bounded aggregates and immutable records. It requires careful aggregate design because a large object graph is loaded as one unit and a save can rewrite owned data. It occupies a middle ground between hand-written [[Spring JdbcClient Fluent Data Access]] and the richer relationship machinery of [[Spring Data JPA Relationship Mapping]].

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
