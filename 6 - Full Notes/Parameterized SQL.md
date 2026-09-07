2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Parameterized SQL

Parameterized SQL keeps variable values separate from the SQL command text. Dapper binds values from an object to named parameters, allowing the database driver to treat them as data rather than executable query fragments.

This is the normal way to pass identifiers, filters, and inserted values into repository queries. It also makes the intended inputs explicit at the point where a command is executed.

# References

[[aspnetcore3andreact.pdf]]
