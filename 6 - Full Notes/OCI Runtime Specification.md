2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# OCI Runtime Specification

The OCI Runtime Specification standardizes the configuration and lifecycle contract for running an isolated filesystem bundle. Its configuration describes the process, root filesystem, mounts, namespaces, capabilities, and other Linux settings that an implementation must apply when creating a container.

Runtimes such as runc and [[crun Container Runtime]] consume this contract, allowing a [[Container Engine]] to delegate process creation without binding its entire architecture to one runtime implementation. The runtime specification concerns execution; the separate [[OCI Image Specification]] concerns how distributable image content is packaged.

# References

[[podmanfordevopssecondedition.pdf]]
