2026-09-08 21:16

Status: #baby

Tags: [[Entity Framework Core Data Access]]

# EF Core Database Context

A `DbContext` represents an application's session with a database. It exposes entity sets for queries, coordinates model metadata, tracks changes to loaded entities, and translates a unit of work into database commands when changes are saved.

The context is intended to have a bounded lifetime rather than act as a global object. Short, explicit units of work limit accumulated tracking state and align naturally with a web request or another application operation.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
