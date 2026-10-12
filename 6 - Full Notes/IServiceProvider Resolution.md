2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# IServiceProvider Resolution

`IServiceProvider` resolves services according to the registrations held by a .NET dependency-injection container. It can create a requested service and recursively provide the constructor dependencies registered for that service. In the book's test, rebuilding a provider for every lookup also rebuilt its supposedly singleton inventory context; singleton identity belongs to one provider instance, not to every provider built from equivalent registrations.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

