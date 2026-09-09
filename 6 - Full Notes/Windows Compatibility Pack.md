2026-09-08 21:16

Status: #baby

Tags: [[.NET Windows Desktop Applications]] [[Windows Desktop Modernization]]

# Windows Compatibility Pack

The Windows Compatibility Pack provides additional APIs for .NET Core applications that run on Windows and need functionality familiar from the .NET Framework. It helps port code whose required operations are inherently tied to the Windows platform.

Adding the pack can reduce migration effort, but it does not make those APIs cross-platform. The dependency should be isolated and documented so portable application code is not accidentally coupled to Windows-specific behavior.

The photo-storage project uses the pack to recover Windows-specific APIs that were not part of the cross-platform .NET Core surface, including the APIs needed to implement a Windows Service. This preserves a deliberate platform dependency while allowing the rest of the project to target .NET Core 3.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
