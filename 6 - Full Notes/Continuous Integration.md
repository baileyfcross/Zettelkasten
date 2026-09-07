2026-09-05 15:58

Status: #baby

Tags: [[Agile Engineering and Quality]], [[Continuous Integration and Delivery]]

# Continuous Integration

Continuous integration merges small changes into the shared codebase frequently and verifies them with automated builds and tests. Failures are reported quickly and repaired before more work accumulates on an unstable base.

Its value is short integration feedback, not merely operating a build server. Small commits, dependable tests, and collective attention to broken builds keep the shared game usable.

For a React and ASP.NET Core application, an Azure DevOps build pipeline can trigger from the source repository, compile both applications, run automated tests, and publish versioned artifacts. This turns each accepted revision into rapid, repeatable evidence about whether it is ready to enter the release flow.

# References

[[agilegamedevelopment2e.pdf]]
[[aspnetcore3andreact.pdf]]
