2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut Data Repository

A Micronaut Data repository is an annotated interface that extends a repository contract for a domain type and identifier type. The framework supplies its implementation, including common operations such as save, find by identifier, find all, and delete.

The book combines CrudRepository interfaces with persistence-mapped Product, Quote, and QuoteLine entities. A controller receives the repository through constructor injection and delegates storage operations to it, avoiding a handwritten implementation while retaining a typed boundary between HTTP handling and persistence.

# References

[[prorestfulapiswithmicronaut.epub]]
