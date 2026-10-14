2026-10-11 21:26

Status: #baby

Tags: [[Docker Container Security]]

# Container No-New-Privileges

Container no-new-privileges prevents a process and its descendants from gaining privileges beyond those available at execution, including through set-user-ID binaries. In Docker it is applied as a runtime security option and complements running as a non-root user and dropping capabilities.

The control does not remove authority already granted to the container, so it cannot compensate for privileged mode, broad host mounts, or an excessive capability set. It narrows one escalation path within a defense-in-depth configuration whose other boundaries still need independent review.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
