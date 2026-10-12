2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]] [[Aggregate Consistency and Persistence]] [[ASP.NET Core Service Layers and Mapping]]

# Repository Pattern

The repository pattern places persistence operations behind an application-facing interface. Controllers request domain data through repository methods instead of embedding connections and SQL inside HTTP actions.

With Dapper, the repository owns query text, parameters, result mapping, and connection behavior. This boundary makes callers less dependent on the chosen access mechanism and gives tests a replaceable data collaborator.

The inventory example first puts books in an in-memory repository shared by add, update, and get commands, then plans to replace that store with persistent data. The command logic can stay focused on its operation because the repository interface, not the initial storage choice, is its dependency.

In Domain-Driven Design, a repository represents a collection of [[Aggregate]] roots and abstracts their persistence from the domain and application layers. Its interface can load or add an aggregate while a separate [[Unit of Work]] owns the commit. A repository should not become a generic query layer for arbitrary screens: aggregate behavior belongs on the command side, while [[Read Model]] queries can use storage directly when that better matches their purpose.

In an ASP.NET Core REST service, the repository boundary also lets the application layer select between Entity Framework Core, Dapper, or a test double without forcing controllers to understand provider-specific query mechanics.

This book reinforces aggregate-centric repositories: the application layer depends on an interface for loading and storing roots, while provider-specific implementations are supplied through dependency injection.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andreact.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
[[hands-ondomain-drivendesignwithnetcore.pdf]]

[[hands-onmobiledevelopmentwithnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
