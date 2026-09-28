2026-09-27 11:48

Status: #baby

Tags: [[Continuous Delivery Risk and Release Governance]]

# Manual Deployment Approval

Manual deployment approval requires a named person or group to authorize a release transition. It is appropriate where business timing, regulation, coordinated operations, or evidence interpretation cannot be reduced to an automated condition.

The approval should record who decided, what artifact was approved, and which evidence was considered. Adding a person who merely clicks through every release increases delay without reducing risk.

For infrastructure delivery, the approval can bind a reviewed [[Terraform Plan]] to the later apply step so the approver sees additions, changes, and deletions before production mutation. The pipeline should invalidate or regenerate approval when the plan or configuration changes; otherwise the person may authorize evidence that no longer describes the deployment.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
[[clouddevopsengineersguide.pdf]]
