2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Repository Pattern

The repository pattern places persistence operations behind an application-facing interface. Controllers request domain data through repository methods instead of embedding connections and SQL inside HTTP actions.

With Dapper, the repository owns query text, parameters, result mapping, and connection behavior. This boundary makes callers less dependent on the chosen access mechanism and gives tests a replaceable data collaborator.

The inventory example first puts books in an in-memory repository shared by add, update, and get commands, then plans to replace that store with persistent data. The command logic can stay focused on its operation because the repository interface, not the initial storage choice, is its dependency.

# References

[[aspnetcore3andreact.pdf]]
[[hands-ondesignpatternswithcandnetcore.pdf]]
