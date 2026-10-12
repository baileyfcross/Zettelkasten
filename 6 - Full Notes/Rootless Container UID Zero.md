2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Rootless Container UID Zero

Rootless container UID zero is the namespace-local root identity mapped to an unprivileged host user. It can perform operations allowed within that user namespace, but it is not the host's UID 0 and cannot bypass host permissions merely because tools inside the container display `root`.

This is safer than host root, yet an application should still run as a nonzero container user when possible. Doing so narrows privileges inside the namespace, improves compatibility with orchestrated policy, and avoids making every file in the image or mounted data appear owned by the most powerful identity available within the container.

# References

[[podmanfordevopssecondedition.pdf]]
