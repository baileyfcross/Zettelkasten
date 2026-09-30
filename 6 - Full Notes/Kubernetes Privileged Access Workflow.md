2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Multitenancy and Secure Interfaces]]

# Kubernetes Privileged Access Workflow

A Kubernetes privileged access workflow grants elevated authority temporarily for a specific operational need rather than leaving administrator permissions attached to a user's daily identity. Approval, a distinct privileged subject or controlled impersonation path, short lifetime, and complete auditing make the elevation attributable.

The workflow should also define how access is revoked and how emergency actions are reviewed. Merely asking operators to use an administrator account carefully does not limit credential theft, stale membership, or accidental high-impact commands.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]
