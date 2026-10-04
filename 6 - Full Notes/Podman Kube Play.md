2026-10-04 08:37

Status: #baby

Tags: [[Podman Workload Integration and Desktop]]

# Podman Kube Play

Podman kube play reads Kubernetes YAML and creates corresponding local pods, containers, networks, volumes, and services where supported. It lets a developer exercise a declarative workload through Podman without first deploying a multi-node cluster.

The command is a compatibility bridge, not a local implementation of every Kubernetes controller. Testing should distinguish resources Podman realizes directly from behaviors supplied only by a cluster, such as scheduling, replica reconciliation, dynamic storage, ingress, or cloud integrations. [[Podman Kube Generate]] supports the reverse path from local objects to YAML.

# References

[[podmanfordevopssecondedition.pdf]]
