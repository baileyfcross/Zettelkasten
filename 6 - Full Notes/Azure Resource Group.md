2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure Resource Group

An Azure resource group is a management container for related cloud resources. The book places the application's App Services, service plan, and SQL resources into a shared group so they can be viewed and managed as one deployed system.

The group provides an operational boundary rather than an application runtime. Naming and environment separation should make it clear which resources belong together and which lifecycle they share.

The Azure projects group databases, applications, monitoring tools, and related services by shared purpose and lifetime. Because deleting a group removes its contained resources, it also becomes a practical cleanup boundary for temporary project infrastructure.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andreact.pdf]]
