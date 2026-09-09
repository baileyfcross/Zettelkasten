2026-09-08 22:09

Status: #baby

Tags: [[Windows Desktop Modernization]]

# ProcessStartInfo

`ProcessStartInfo` describes how .NET should start another process, including the target file, arguments, working directory, and whether the operating-system shell participates. The e-book manager uses process launching to open a selected document or its location.

External process behavior depends on the target environment and registered file associations, so launch failures should be handled as boundary errors. Keeping the launch configuration in one object makes those assumptions explicit before the process is started.

# References

[[c8andnetcore30projectsusingazure.pdf]]
