2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Service Layers and Mapping]]

# Repository Interface

A repository interface states the persistence operations needed by an application service without fixing their implementation. Methods can retrieve, add, update, delete, or query domain entities while an Entity Framework or Dapper adapter supplies the actual storage behavior.

The interface should follow application needs rather than mirror every database operation. It creates a dependency boundary for tests, but an excessively generic contract can hide important query and transaction semantics.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
