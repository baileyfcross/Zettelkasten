2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Micro ORM

A micro ORM provides a small layer between application objects and relational query results. It commonly handles parameter binding and row-to-object mapping while leaving SQL creation and relational behavior explicit.

Dapper follows this model: it reduces low-level ADO.NET ceremony without becoming the owner of the database model. The tradeoff is that the application must deliberately design and maintain its SQL.

# References

[[aspnetcore3andreact.pdf]]
