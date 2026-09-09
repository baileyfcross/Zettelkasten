2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]] [[Angular Application Architecture]] [[ASP.NET Core Page and MVC Development]]

# Dependency Injection

Dependency injection supplies an object with its collaborators instead of making it construct or locate them itself. This reduces hard-coded dependencies and supports reuse, readability, configuration, and isolated testing.

ASP.NET Core registers application services during startup and injects them into consumers such as controllers. Angular applies the same design principle to components and services, allowing an [[Angular HttpClient]] or a custom [[Data Service]] to be supplied through a constructor.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
