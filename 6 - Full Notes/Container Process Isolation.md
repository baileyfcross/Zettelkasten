2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# Container Process Isolation

Container process isolation gives an application a constrained view of the host rather than a separate kernel. Filesystem mounts, process identifiers, users, networks, inter-process communication, and resource accounting can each be isolated so several applications and dependency sets coexist without seeing the same system state.

The isolation is assembled from native Linux facilities. [[Linux Namespace Isolation]] controls visibility, while [[Linux Control Groups]] account for and limit resource use. A [[Container Engine]] coordinates those mechanisms with an image and an [[OCI Container Runtime]], which makes a container a managed process environment rather than a miniature virtual machine.

# References

[[podmanfordevopssecondedition.pdf]]
