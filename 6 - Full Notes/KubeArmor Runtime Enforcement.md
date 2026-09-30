2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# KubeArmor Runtime Enforcement

KubeArmor applies workload-aware runtime security policies to process execution, file access, and network behavior. It connects Kubernetes identity and policy to Linux enforcement facilities such as AppArmor or SELinux and uses eBPF-based visibility where appropriate.

This complements admission control: Gatekeeper decides whether a pod specification may be created, while KubeArmor constrains what an accepted workload may do after it starts. Policies should be observed and tuned before blocking so normal application behavior is not mistaken for an attack.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

