2026-09-08 21:16

Status: #baby

Tags: [[.NET Windows Desktop Applications]] [[Windows Desktop Modernization]]

# Windows Forms on .NET Core

.NET Core 3.0 brought Windows Forms support to the newer .NET runtime for Windows applications. Existing event-driven forms and controls could use modern project tooling while remaining tied to the Windows desktop environment.

Porting is not guaranteed to be a simple runtime switch because applications may depend on libraries or APIs absent from .NET Core. Compatibility analysis and targeted testing identify which pieces can move and which require replacement.

The Azure projects book demonstrates a 2019-era migration by changing a legacy Windows Forms project to the Windows Desktop SDK, targeting `netcoreapp3.0`, enabling Windows Forms, and then resolving package, reference, and resource differences. The interface can remain familiar while the runtime and project system change.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
