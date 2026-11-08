2026-11-08 14:08

Status: #baby

Tags: [[Jakarta Persistence and Data Access]]

# Jakarta Data Repository

Jakarta Data defines repository interfaces whose method signatures state data-access intent while a runtime supplies their implementations. Built-in interfaces range from the minimal DataRepository through BasicRepository to CrudRepository, and a repository may add query-derived methods, annotated queries, and offset- or cursor-based pagination.

The abstraction is designed to work over both Jakarta Persistence and Jakarta NoSQL rather than replacing either specification. Its supported operations still depend on the selected data-store category, but the repository contract gives application code a consistent entry point across relational and non-relational implementations and reduces repeated DAO plumbing.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
