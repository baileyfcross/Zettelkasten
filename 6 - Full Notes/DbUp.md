2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# DbUp

DbUp is a .NET library for applying ordered database change scripts. It records which scripts have run, discovers pending scripts, and executes them so the database schema advances with the application.

The book configures migrations during application startup and packages SQL as embedded resources. A production workflow should still control when and under which identity those schema-changing operations execute.

# References

[[aspnetcore3andreact.pdf]]
