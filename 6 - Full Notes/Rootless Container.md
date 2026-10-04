2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Rootless Container

A rootless container is created and managed by an ordinary host user without a privileged container-engine daemon. A user namespace maps container identities into subordinate host IDs, and per-user storage, runtime files, sockets, and networks keep one user's containers separate from another's.

Rootless execution reduces the authority available after a container escape, but it is not a universal security boundary. Host kernel vulnerabilities, broad mounts, excessive capabilities, permissive labels, and exposed credentials still matter. It also changes storage permissions, networking, and privileged-port behavior, so a rootful workload cannot always be migrated by changing only the invoking user.

# References

[[podmanfordevopssecondedition.pdf]]
