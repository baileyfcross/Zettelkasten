2026-09-06 20:37

Status: #baby

Tags: [[Web Application Testing]]

# In-Memory Database Provider

An in-memory database provider stores test data in process instead of connecting Entity Framework Core to the production database server. It gives a test a fast, disposable context with known records.

This supports isolated controller tests without a SQL Server dependency. Because the provider does not reproduce every relational database behavior, it is a unit-testing aid rather than proof that production SQL integration works identically.

# References

[[aspnetcore3andangular9_3ed.pdf]]
