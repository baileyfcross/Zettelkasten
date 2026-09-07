2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# Framework-Dependent Deployment

A framework-dependent deployment publishes an application without bundling the full .NET runtime. The target machine must already have a compatible shared runtime installed.

This produces a smaller deployment and allows installed runtime servicing to be shared among applications, but the application's execution depends on the target's runtime availability. A [[Self-Contained Deployment]] carries its own runtime instead.

# References

[[aspnetcore3andangular9_3ed.pdf]]
