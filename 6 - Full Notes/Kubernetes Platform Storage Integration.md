2026-10-03 22:25

Status: #baby

Tags: [[Kubernetes Platform Infrastructure]]

# Kubernetes Platform Storage Integration

Kubernetes platform storage integration uses the Container Storage Interface to connect portable workload declarations with provider or software-defined storage. A CSI driver translates claims and storage classes into volumes, attachments, snapshots, and other operations supplied by the underlying system.

The abstraction does not make storage interchangeable without qualification. Drivers may require cloud permissions, snapshot components, node-level privileges, topology knowledge, and provider-specific behavior. A platform should define supported classes, durability and recovery expectations, access modes, and security boundaries so that self-service claims produce predictable storage rather than merely successful provisioning.

# References

[[platformengineeringforarchitects.pdf]]
