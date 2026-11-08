2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Service Layers and Mapping]]

# Repository Interface

A repository interface states the persistence operations needed by an application service without fixing their implementation. Methods can retrieve, add, update, delete, or query domain entities while an Entity Framework or Dapper adapter supplies the actual storage behavior.

The interface should follow application needs rather than mirror every database operation. It creates a dependency boundary for tests, but an excessively generic contract can hide important query and transaction semantics.

Jakarta Data standardizes this idea with repository interfaces whose implementations are supplied at runtime. DataRepository, BasicRepository, and CrudRepository offer progressively richer built-in contracts, while application interfaces can add query-derived methods or annotated queries. The uniform interface can sit over Jakarta Persistence or Jakarta NoSQL, although the chosen store still determines which operations are supported.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
