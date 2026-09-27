2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Release Pipeline

A release pipeline takes versioned build artifacts and installs them into one or more deployment environments. In the book, the flow targets Azure staging resources before promoting a verified release to production.

Separating release from build means the same tested artifact can move between environments. Environment configuration and promotion conditions remain part of the release definition rather than the compiled package.

The architecture case study configures release stages, environment settings, and a manual approval before production. The release pipeline consumes the build artifact rather than treating deployment as an unrecorded command from a workstation.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andreact.pdf]]
