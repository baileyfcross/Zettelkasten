2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Build Pipeline

A build pipeline is the automated sequence that turns a source revision into verified deployment artifacts. It restores dependencies, compiles the React and ASP.NET Core applications, runs selected tests, and publishes the outputs needed by the release process.

Every result belongs to a particular source version. A failed required step stops that version from being treated as a releasable artifact.

# References

[[aspnetcore3andreact.pdf]]
