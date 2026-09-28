2026-09-27 18:58

Status: #baby

Tags: [[AWS AI and Infrastructure Automation]]

# AWS CodeDeploy

AWS CodeDeploy automates software deployment to supported compute targets, including EC2 instances, Lambda functions, and ECS services. Deployment configuration controls how quickly the new revision replaces or shifts traffic away from the old one.

Automation makes releases repeatable, but a safe deployment also needs health validation and rollback criteria. In-place and blue-green strategies make different tradeoffs among speed, extra capacity, and the ability to return to the prior version.

In a blue-green deployment, the new revision is prepared in a separate replacement environment and traffic moves only after validation. This costs temporary duplicate capacity but makes the prior environment available for rapid rollback. Hooks and health checks must test application readiness rather than merely confirm that a process started.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[clouddevopsengineersguide.pdf]]
