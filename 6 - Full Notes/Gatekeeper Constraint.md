2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Gatekeeper Constraint

A Gatekeeper Constraint instantiates a ConstraintTemplate with concrete parameters and a match scope. It selects the resource kinds, namespaces, labels, or other admission contexts to which the policy applies.

This division lets one reviewed policy implementation support different organizational rules. Constraint rollout should begin with audit or limited matching, because an overly broad selector or incorrect parameter can deny legitimate system resources as well as tenant workloads.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

