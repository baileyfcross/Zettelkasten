2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Policy and Runtime Security]]

# Kubernetes Host Namespace Restriction

Host namespace settings let a pod share the node's process, network, or IPC namespace. They can support specialized diagnostics or node agents, but they expose host-level information and weaken the separation expected between ordinary workloads and the node.

Admission policy should deny host PID, host IPC, and host networking by default and pair any exception with restricted service accounts, scheduling, and runtime rules. A hostPath volume deserves similar treatment because namespace separation is of little value if the pod can rewrite sensitive host files.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

