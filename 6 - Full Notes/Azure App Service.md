2026-09-06 20:52

Status: #baby

Tags: [[Cloud Application Deployment]]

# Azure App Service

Azure App Service is a managed web hosting resource used to run a deployed application. The book uses separate services for the ASP.NET Core backend and the React frontend, allowing each application to have its own address and deployment artifact.

Managed hosting supplies the execution environment, while the application still supplies its build output, settings, connection information, and allowed network relationships.

The web-research and bot projects use App Service as the managed destination for ASP.NET Core applications. Visual Studio can create or select the resource during publishing, while application settings configured in the service can override file-based values so secrets need not remain in source.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andreact.pdf]]
