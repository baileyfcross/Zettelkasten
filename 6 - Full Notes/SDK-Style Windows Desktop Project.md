2026-09-08 22:09

Status: #baby

Tags: [[Windows Desktop Modernization]]

# SDK-Style Windows Desktop Project

An SDK-style Windows desktop project uses the compact `Microsoft.NET.Sdk.WindowsDesktop` project format to build Windows Forms or WPF software on .NET Core 3. Properties select the executable type, target framework, language version, and the desktop UI framework used by the project.

Package and project references are declared explicitly in the project file, which makes the build inputs easier to inspect than older verbose formats. A successful conversion still requires testing because changing the project system can expose missing assemblies, unsupported APIs, or files that were previously copied implicitly.

# References

[[c8andnetcore30projectsusingazure.pdf]]
