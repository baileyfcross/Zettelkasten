2026-09-06 20:34

Status: #baby

Tags: [[Entity Framework Core Data Modeling]] [[Entity Framework Core Data Access]]

# Database-First Development

Database-first development begins with an existing database and derives application entity classes and mappings from its schema. It is useful when the database already exists or is controlled separately from the application code.

Schema changes originate in the database and may require regenerated or updated application mappings. This reverses the direction used by [[Code-First Development]], where entity classes and migrations lead the schema.

For EF Core 3, the book describes database-first as a one-way starting operation: tooling can reverse-engineer a code model from an existing schema, but subsequent database changes are generated from the resulting code model rather than continuously synchronized both ways.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
