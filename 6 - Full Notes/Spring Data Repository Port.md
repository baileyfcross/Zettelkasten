2026-10-30 17:24

Status: #baby

Tags: [[Spring Data Access and Persistence]]

# Spring Data Repository Port

A Spring Data repository interface can serve as a driven persistence port. Extending a repository contract supplies common CRUD declarations, while domain-specific query methods add only the operations the application needs.

Spring creates the concrete adapter from the chosen data dependency and configuration at runtime. The application calls the interface, so a repository boundary can remain stable while PostgreSQL and MongoDB implementations differ behind it.

The Spring Boot 4 source shows the same repository model across Spring Data JDBC, JPA, MongoDB, and R2DBC, while retaining each store's specific mapping and execution traits. Ahead-of-time repository processing can pre-generate query and proxy work for a native build, improving startup but making unsupported dynamic behavior visible during the build or native test.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[javamicroservicesandcontainersinthecloud.epub]]

