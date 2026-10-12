2026-09-27 18:58

Status: #baby

Tags: [[AWS AI and Infrastructure Automation]]

# AWS CloudFormation Change Set

An AWS CloudFormation change set previews the resource actions that a proposed template or parameter update would apply to an existing stack. It distinguishes additions, modifications, replacements, and removals before the operator executes the update.

The preview reduces surprise, especially when changing a property would replace a stateful resource. It is not a proof that the update will succeed or preserve application behavior, so backups, testing, dependency awareness, and rollback planning remain necessary.

# References

[[awscertifiedcloudpractitionerclf-c02certificationguidesecondeditio.pdf]]
