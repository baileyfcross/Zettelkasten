2026-09-27 18:58

Status: #baby

Tags: [[AWS AI and Infrastructure Automation]]

# AWS CloudFormation Stack

An AWS CloudFormation stack is a managed instance of the resources declared in an [[AWS CloudFormation Template]]. CloudFormation treats those related resources as one unit for creation, update, status tracking, and deletion.

If an operation fails, stack events reveal which resource caused the problem, and rollback can return the stack toward its prior state. Resources modified outside CloudFormation can create drift between declared and actual configuration, so infrastructure changes should follow a consistent management path.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
