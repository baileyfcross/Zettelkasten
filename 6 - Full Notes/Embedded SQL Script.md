2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Embedded SQL Script

An embedded SQL script is a database change file packaged as an application assembly resource. DbUp can discover these resources by name, compare them with its migration journal, and execute the scripts that have not yet been applied.

Embedding makes the schema changes travel with the application version. A stable naming order ensures that dependent changes run in the intended sequence.

# References

[[aspnetcore3andreact.pdf]]
