2026-09-06 20:52

Status: #baby

Tags: [[Dapper Data Access]]

# Database Migration

A database migration is an ordered, repeatable change that advances a database schema or required data from one version to the next. Applied migrations are journaled so the same change is not executed again on a later startup.

Migration scripts allow the database and application to evolve together. They should be additive and reviewable enough that deployment can determine what will change before the new application depends on it.

# References

[[aspnetcore3andreact.pdf]]
