2026-09-27 18:58

Status: #baby

Tags: [[AWS AI and Infrastructure Automation]]

# AWS CodeBuild

AWS CodeBuild is a managed build service that runs commands defined for a software project, such as compiling source, executing tests, and packaging artifacts. It provisions isolated build capacity on demand, streams logs, and returns a success or failure result.

CodeBuild removes the need to maintain a permanent fleet of build servers. Within an [[AWS CodePipeline]], its result can act as a quality gate before artifacts proceed to deployment.

The project can take source and dependencies, follow commands in a build specification, publish versioned artifacts, and stream output to operational logs. Its execution role should have only the permissions needed for inputs, outputs, and deployment preparation. A reproducible build must not rely on undeclared state left behind by an earlier ephemeral worker.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[clouddevopsengineersguide.pdf]]
