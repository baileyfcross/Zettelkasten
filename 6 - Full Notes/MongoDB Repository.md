2026-09-08 22:09

Status: #baby

Tags: [[Azure Cosmos DB Applications]]

# MongoDB Repository

A MongoDB repository encapsulates creation of the Mongo client, selection of a database, and access to document collections. Moving this work out of an MVC controller gives the application one reusable place to handle connection setup and data-access failures.

In the Cosmos project, the repository receives settings through configuration and exposes the work-item collection used by a service. This boundary keeps database-specific driver code separate from request handling and makes later replacement or testing less invasive.

In the Spring example, a repository interface extends `MongoRepository` or the more generic `CrudRepository`, and Spring creates the MongoDB adapter from dependencies and runtime configuration. The controller and service call the port, allowing the same core behavior to be demonstrated with a PostgreSQL adapter in another configuration.

# References

[[c8andnetcore30projectsusingazure.pdf]]
[[javamicroservicesandcontainersinthecloud.epub]]
