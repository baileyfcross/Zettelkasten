2026-11-08 16:45

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Neo4jClient

Spring `Neo4jClient` is a fluent interface for executing Cypher, binding parameters, fetching results, and participating in Spring-managed resource and transaction handling. It gives an application direct control over graph pattern queries without requiring every relationship to be expressed through object-graph mapping.

Bound variables protect values from Cypher injection, while recursive relationship patterns can traverse an ownership hierarchy to arbitrary supported depth. The client is appropriate when graph-native queries are central and explicit Cypher is clearer than a generated repository. In a polyglot service, it can coexist with PostgreSQL master data and Redis transient state behind separate repository boundaries.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
