2026-09-30 23:18

Status: #baby

Tags: [[Terraform Utility Providers and Artifacts]]

# Terraform Time Provider

The Terraform time provider represents timestamps, delays, rotations, and offsets as managed resources. Because its values participate in the [[Terraform Dependency Graph]], it can model a waiting period after one resource becomes available or trigger periodic replacement without hiding timing logic in a shell script.

Time-based behavior should still match the remote system's semantics. A fixed sleep can mask a missing readiness signal and make automation slower or less reliable, while rotation resources can cause real replacement on the next [[Terraform Apply]]. The provider is best used when time is genuinely part of the desired lifecycle rather than a workaround for an unknown dependency.

# References

[[masteringterraform.pdf]]

