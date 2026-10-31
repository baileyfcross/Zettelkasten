2026-10-30 17:24

Status: #baby

Tags: [[Spring Microservice Application Architecture]]

# Spring MongoRepository Adapter

A Spring `MongoRepository` adapter binds a repository interface to MongoDB and supplies default create, retrieve, update, and delete operations for a document type and identifier type. Custom finder declarations can extend that generated behavior without writing the adapter implementation directly.

Database connection properties and the Spring Data MongoDB dependency select the concrete infrastructure. The consuming controller or service continues to work through the repository port rather than through the MongoDB driver.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

