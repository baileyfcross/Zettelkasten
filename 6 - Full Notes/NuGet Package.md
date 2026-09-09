2026-09-08 21:16

Status: #baby

Tags: [[.NET Assemblies Packages and Deployment]]

# NuGet Package

A NuGet package is a versioned distribution containing .NET assemblies and optional supporting resources and metadata. A project reference declares the package and version, after which restore retrieves it and its dependencies.

Library authors can package their own compiled code with identity, description, and compatibility information. Consumers should pin concrete compatible versions rather than wildcards or prerelease qualifiers when reproducible restoration matters.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
