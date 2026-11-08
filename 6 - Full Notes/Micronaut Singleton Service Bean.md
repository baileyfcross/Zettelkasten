2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut Singleton Service Bean

A Micronaut service marked Singleton becomes a container-managed component with one application-scoped instance. Controllers can declare the service as a constructor dependency, letting the framework supply it without the controller constructing or locating the implementation.

The book places message CRUD behavior in such a service while the controller retains HTTP routing and body binding. This division makes the service reusable outside one endpoint and keeps transport decisions separate from application operations, even when the example initially stores data only in memory.

# References

[[prorestfulapiswithmicronaut.epub]]
