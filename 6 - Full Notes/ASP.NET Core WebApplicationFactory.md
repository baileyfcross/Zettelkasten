2026-09-27 11:07

Status: #baby

Tags: [[ASP.NET Core API Integration Testing]]

# ASP.NET Core WebApplicationFactory

`WebApplicationFactory<TEntryPoint>` creates an in-process test host from an ASP.NET Core application's entry point. Tests obtain an `HttpClient` from the factory and send ordinary HTTP requests through the configured middleware, routing, model binding, filters, controllers, and services.

The factory is an integration-testing boundary rather than a substitute for unit tests. It verifies that the assembled application behaves correctly without requiring a separately deployed web server.

The software-architecture source recommends `Microsoft.AspNetCore.Mvc.Testing` for controlled functional tests, creating both an in-process server and HTTP client so middleware and application composition participate in the acceptance path.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
