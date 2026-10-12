2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Kubernetes Privileged Container Restriction

A privileged container receives broad host-like authority and can bypass many ordinary isolation mechanisms. Restricting the `privileged` setting, capability additions, device access, and privilege escalation prevents application teams from silently converting a pod compromise into a node compromise.

Some infrastructure agents may require exceptional access, so policy should use narrowly matched exemptions owned by the platform team. Treating every daemon as an exception erodes the boundary and makes admission policy ceremonial rather than protective.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

