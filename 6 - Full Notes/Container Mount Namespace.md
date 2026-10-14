2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# Container Mount Namespace

A container mount namespace isolates the list and arrangement of mount points visible to a process. It can expose an alternative directory tree containing the required binaries and libraries while hiding the host's ordinary filesystem layout.

Mount namespaces work with bind mounts and layered image storage. The runtime assembles image layers into one filesystem view, attaches required files such as resolver configuration, and starts the process inside that view. This filesystem boundary is a central part of [[Linux Namespace Isolation]], but access still depends on permissions and controls such as SELinux.

# References

[[podmanfordevopssecondedition.pdf]]
