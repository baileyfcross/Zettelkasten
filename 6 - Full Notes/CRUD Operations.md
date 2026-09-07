2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# CRUD Operations

CRUD operations are the create, read, update, and delete behaviors through which an application manages persistent records. A Dapper repository implements them with explicit SQL or stored procedures and maps the affected values back to application types.

These operations form a persistence vocabulary, but each endpoint still needs domain rules, validation, and meaningful outcomes. Treating CRUD as a transport pattern does not remove the application's responsibility for valid state transitions.

# References

[[aspnetcore3andreact.pdf]]
