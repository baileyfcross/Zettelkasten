2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# Application Configuration

Application configuration separates adjustable settings from the code that consumes them. In an ASP.NET Core project, root files such as `Program.cs`, `Startup.cs`, and `appsettings.json` coordinate hosting, services, middleware, compilation, and publication behavior.

Environment-specific files can override general values for a [[Development Environment]], [[Staging Environment]], or [[Production Environment]]. Configuration values may be read by key or bound to typed classes so the rest of the application uses a defined model.

# References

[[aspnetcore3andangular9_3ed.pdf]]
