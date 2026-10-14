2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# Podman Daemonless Architecture

Podman's daemonless architecture performs container operations through a fork-and-exec model instead of routing every command through a privileged, always-running engine daemon. The Podman process works with [[Libpod]], image and storage libraries, [[Conmon]], and an [[OCI Container Runtime]], then exits while the container workload continues.

This removes an engine daemon as a single lifecycle dependency and makes per-user rootless operation natural. Podman can still expose a socket-activated REST service for clients that need an API, but the service is an optional interface rather than the mandatory owner of every container.

# References

[[podmanfordevopssecondedition.pdf]]
