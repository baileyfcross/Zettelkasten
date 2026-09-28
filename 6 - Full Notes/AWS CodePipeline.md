2026-09-27 18:58

Status: #baby

Tags: [[AWS AI and Infrastructure Automation]]

# AWS CodePipeline

AWS CodePipeline coordinates a release as a sequence of stages and actions. A source change can flow through build, test, approval, and deployment steps using services such as [[AWS CodeBuild]] and [[AWS CodeDeploy]].

The pipeline defines the path an artifact must follow and stops when an action fails, making delivery repeatable and auditable. The quality of the release still depends on the tests, approvals, permissions, and rollback behavior configured in those actions.

An end-to-end path can obtain source, use [[AWS CodeBuild]] to test and package it, preserve the resulting artifact between stages, pause for an approval, and invoke [[AWS CodeDeploy]]. Keeping the artifact identity unchanged across promotion prevents production from receiving a build that was never tested, while stage-specific IAM roles constrain what each action may change.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
[[clouddevopsengineersguide.pdf]]
