2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Identity Access and Secrets]]

# Kubernetes Audit Policy

A Kubernetes audit policy selects which API requests are recorded and how much of each event is retained. Rules can match users, verbs, resources, namespaces, and non-resource URLs, with levels ranging from metadata to request and response bodies.

Audit detail must balance investigation needs against volume and secret exposure. Logs should reach a protected external destination, and the policy should capture privileged changes, authorization-sensitive actions, and impersonation without indiscriminately recording confidential object contents.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

