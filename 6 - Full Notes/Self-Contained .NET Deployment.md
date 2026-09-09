2026-09-08 21:16

Status: #baby

Tags: [[.NET Assemblies Packages and Deployment]]

# Self-Contained .NET Deployment

A self-contained .NET deployment includes the application, its dependencies, and the runtime required to execute it. The target does not need a separately installed compatible runtime, making the published bundle more predictable and portable to the selected platform.

That independence increases output size and requires a runtime identifier for the intended operating system and architecture. Separate bundles may be needed for different targets, and the application owner carries responsibility for updating the included runtime.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
