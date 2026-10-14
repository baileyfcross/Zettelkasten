2026-10-04 08:37

Status: #baby

Tags: [[Podman Networking and Diagnostics]]

# Pod Infra Container

A Pod infra container is the small process that holds the shared namespaces of a [[Podman Pod]]. Other containers join those namespaces, so the pod's network identity and related resources remain stable even as individual application containers start and stop.

The infra container is infrastructure for the pod rather than an application component. Inspecting it helps explain why ports are published for the pod as a unit and why containers in the pod see the same loopback interface, while application logs and lifecycle commands remain attached to their individual containers.

# References

[[podmanfordevopssecondedition.pdf]]
