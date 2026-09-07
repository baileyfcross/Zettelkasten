2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure SQL Database

Azure SQL Database is the managed relational database used by the deployed ASP.NET Core backend. The application connects through an environment-specific connection string and applies the schema required by its repository queries.

Deployment must configure network access and credentials as well as create the database resource. A successful web deployment is incomplete if the API cannot reach a compatible database.

# References

[[aspnetcore3andreact.pdf]]
