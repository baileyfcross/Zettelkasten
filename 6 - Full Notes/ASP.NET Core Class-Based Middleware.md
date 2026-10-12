2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# ASP.NET Core Class-Based Middleware

Class-based ASP.NET Core middleware places request-processing behavior in a type whose constructor receives the next request delegate and whose invocation method receives the current HTTP context. An extension method can expose a clear registration call on the application builder.

The middleware instance follows framework construction rules while per-request services should be resolved at invocation. The class boundary is useful when behavior needs dependencies, tests, and configuration beyond a small inline delegate.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
