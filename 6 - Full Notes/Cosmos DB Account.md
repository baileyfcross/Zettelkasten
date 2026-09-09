2026-09-08 22:09

Status: #baby

Tags: [[Azure Cosmos DB Applications]]

# Cosmos DB Account

A Cosmos DB account is the Azure resource that establishes the database service's globally unique endpoint, API model, location, and distribution settings. It exists inside an Azure subscription and resource group and contains the databases and collections used by an application.

The account name becomes part of a public Azure domain, so naming and environment separation must be planned. Connection strings obtained from the account allow clients to authenticate and locate the service, and should be supplied through configuration rather than embedded in controllers.

# References

[[c8andnetcore30projectsusingazure.pdf]]
