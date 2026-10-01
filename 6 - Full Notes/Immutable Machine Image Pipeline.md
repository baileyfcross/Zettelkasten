2026-09-30 23:18

Status: #baby

Tags: [[Terraform Cloud Deployment Patterns]]

# Immutable Machine Image Pipeline

An immutable machine-image pipeline builds application files, operating-system settings, and dependencies into a versioned image before infrastructure deployment. Tools such as Packer launch a temporary builder, configure it, create the image, and publish its identifier for a later [[Terraform VM Deployment Pipeline]].

Replacing instances from a tested image produces more consistent environments than repeatedly patching servers in place. It also makes rollback a version-selection decision. Build-time credentials and temporary network access should be short-lived, while image identifiers flow through reviewed configuration. Small startup differences can remain in [[Terraform Cloud-Init Configuration]], but heavy provisioning at boot weakens immutability and lengthens recovery.

# References

[[masteringterraform.pdf]]

