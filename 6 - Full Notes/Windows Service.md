2026-09-08 22:09

Status: #baby

Tags: [[Windows Desktop Modernization]]

# Windows Service

A Windows Service is a background application managed by the operating system and intended to run without an interactive user interface. The photo-storage project uses one to monitor a directory and upload files while the user is not actively running a desktop program.

A continuously running service consumes machine resources and is harder to inspect than an interactive application, so performance, logging, startup configuration, and clean shutdown matter. The .NET Core 3 example reaches the required Windows APIs through the [[Windows Compatibility Pack]].

# References

[[c8andnetcore30projectsusingazure.pdf]]
