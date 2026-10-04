2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# Conmon

Conmon is the monitor process that Podman places between container management and an [[OCI Container Runtime]]. After the runtime creates the container, Conmon stays associated with the workload to track its main process, preserve the exit status, manage standard input and output, and write container logs.

This monitor lets both the Podman command and the runtime be short-lived without orphaning lifecycle information. It is therefore a small but important part of [[Podman Daemonless Architecture]]: supervision is attached to each container rather than centralized in one engine daemon.

# References

[[podmanfordevopssecondedition.pdf]]
