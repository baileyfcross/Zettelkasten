2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Release Pipeline

A release pipeline takes versioned build artifacts and installs them into one or more deployment environments. In the book, the flow targets Azure staging resources before promoting a verified release to production.

Separating release from build means the same tested artifact can move between environments. Environment configuration and promotion conditions remain part of the release definition rather than the compiled package.

# References

[[aspnetcore3andreact.pdf]]
