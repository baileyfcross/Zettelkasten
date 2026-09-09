2026-09-08 21:16

Status: #baby

Tags: [[.NET Files Streams and Serialization]]

# Cross-Platform File Paths in .NET

File-system paths differ across operating systems in their directory separators, root conventions, and special folders. .NET code remains portable when it avoids assembling paths with literal separators and instead lets the runtime apply the conventions of the current platform.

`Path.Combine` joins path segments safely, while members of `Path` expose separator characters, extensions, file names, and temporary-path facilities. These APIs make path intent explicit and reduce assumptions that would bind an application to Windows, macOS, or Linux.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
