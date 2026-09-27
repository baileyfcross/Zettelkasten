2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Filter Scope

ASP.NET Core filters can be applied globally, to a controller, or to an individual action. Scope determines which requests receive the behavior and participates with filter order in deciding the sequence around action execution.

Global filters suit policies that truly apply to every MVC operation, while attributes make narrower intent visible. A filter that requires dependency injection can be registered through a service-based mechanism rather than constructed as an opaque attribute instance.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
