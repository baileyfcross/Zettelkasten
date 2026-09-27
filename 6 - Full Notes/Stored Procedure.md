2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]] [[ADO.NET Database Access]] [[ASP.NET Core Service Layers and Mapping]]

# Stored Procedure

A stored procedure is a named database routine that can be invoked with parameters. A Dapper repository can specify the procedure name and command type, then map its returned rows in the same manner as an inline query.

Stored procedures place selected data behavior inside the database. The application still needs an explicit contract for parameter names, result columns, and how the procedure evolves with schema changes.

ADO.NET invokes a stored procedure by naming it in a command, setting `CommandType.StoredProcedure`, binding input or output parameters, and selecting an execution method appropriate to the result. The procedure remains database-side code even though the application controls its invocation.

A repository backed by Dapper can call a stored procedure behind its interface, keeping the procedure name and parameters in the data-access layer rather than leaking them into REST controllers.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[aspnetcore3andreact.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
