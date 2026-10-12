2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# Constructor Injection

Constructor injection declares a component's required collaborators as constructor parameters and supplies them when the component is created. The inventory command factory receives its user-interface and inventory-context contracts instead of constructing those classes internally. This makes dependencies visible, allows tests to substitute implementations, and lets the .NET service provider assemble an object graph from registered services.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

