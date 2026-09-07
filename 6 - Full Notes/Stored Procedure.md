2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Stored Procedure

A stored procedure is a named database routine that can be invoked with parameters. A Dapper repository can specify the procedure name and command type, then map its returned rows in the same manner as an inline query.

Stored procedures place selected data behavior inside the database. The application still needs an explicit contract for parameter names, result columns, and how the procedure evolves with schema changes.

# References

[[aspnetcore3andreact.pdf]]
