2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure SQL Database

Azure SQL Database is the managed relational database used by the deployed ASP.NET Core backend. The application connects through an environment-specific connection string and applies the schema required by its repository queries.

Deployment must configure network access and credentials as well as create the database resource. A successful web deployment is incomplete if the API cannot reach a compatible database.

The order-processing project creates an Azure SQL database for the microservice's durable sales orders and connects to it through Entity Framework Core. The database remains outside the container so replicated workers can share persistent state.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andreact.pdf]]
