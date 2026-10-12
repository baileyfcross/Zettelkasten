2026-09-21 22:12

Status: #baby

Tags: [[.NET Dependency Injection and Service Lifetimes]]

# IServiceCollection Registration

`IServiceCollection` records service descriptions for .NET dependency injection. A registration maps a requested interface or class to a concrete implementation and gives it a lifetime, such as `AddTransient`, `AddScoped`, or `AddSingleton`. Startup code builds a provider from this collection, making construction policy explicit in one place instead of scattering `new` expressions through business logic.

# References

[[hands-ondesignpatternswithcandnetcore.pdf]]

