2026-09-29 22:09

Status: #baby

Tags: [[Kubernetes Cluster Architecture and Resources]]

# etcd Cluster State Store

etcd is the strongly consistent key-value store that holds Kubernetes API state. Resource declarations, controller observations, and cluster configuration become durable control-plane data through the [[Kubernetes API Server]], not through ordinary direct database access.

Because etcd represents the cluster's desired state, its health and backup are distinct from application data protection. A usable recovery plan pairs a verified [[Kubernetes etcd Snapshot]] with the certificates and infrastructure needed to restore control-plane access.

# References

[[kubernetes_anenterpriseguidethirdedition.pdf]]

