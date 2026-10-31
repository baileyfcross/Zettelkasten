2026-10-30 17:24

Status: #baby

Tags: [[Spring Microservice Application Architecture]]

# Spring Data Repository Port

A Spring Data repository interface can serve as a driven persistence port. Extending a repository contract supplies common CRUD declarations, while domain-specific query methods add only the operations the application needs.

Spring creates the concrete adapter from the chosen data dependency and configuration at runtime. The application calls the interface, so a repository boundary can remain stable while PostgreSQL and MongoDB implementations differ behind it.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

