2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]] [[ADO.NET Database Access]]

# Stored Procedure

A stored procedure is a named database routine that can be invoked with parameters. A Dapper repository can specify the procedure name and command type, then map its returned rows in the same manner as an inline query.

Stored procedures place selected data behavior inside the database. The application still needs an explicit contract for parameter names, result columns, and how the procedure evolves with schema changes.

ADO.NET invokes a stored procedure by naming it in a command, setting `CommandType.StoredProcedure`, binding input or output parameters, and selecting an execution method appropriate to the result. The procedure remains database-side code even though the application controls its invocation.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[aspnetcore3andreact.pdf]]
