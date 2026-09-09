2026-09-08 21:16

Status: #baby

Tags: [[.NET Windows Desktop Applications]] [[Windows Desktop Modernization]]

# Windows Presentation Foundation on .NET Core

.NET Core 3.0 supported Windows Presentation Foundation as a Windows-only desktop framework. WPF combines XAML-defined interfaces with .NET code, data binding, styles, templates, and a vector-based rendering system.

Moving a WPF application to the newer runtime can modernize deployment and dependencies while preserving its desktop presentation model. Platform-specific integrations and third-party controls still require compatibility verification.

The .NET Core 3 migration discussion treats WPF alongside Windows Forms as an established Windows-only desktop model that can move to the newer runtime. It also presents XAML Islands as a way for WPF or Windows Forms hosts to incorporate selected UWP controls without replacing the whole application.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
