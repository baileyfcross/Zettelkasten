2026-09-08 21:16

Status: #baby

Tags: [[.NET Assemblies Packages and Deployment]]

# Framework-Dependent .NET Deployment

A framework-dependent .NET deployment publishes the application and its package dependencies but relies on a compatible .NET runtime already installed on the target. This keeps the application output smaller and lets several applications share one runtime.

The tradeoff is an external prerequisite: deployment succeeds only where the correct runtime is present. A framework-dependent executable can add a platform-specific launcher while preserving the same reliance on the installed framework.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
