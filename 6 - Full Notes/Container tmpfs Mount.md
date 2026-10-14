2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]] [[Docker Storage and Configuration]]

# Container tmpfs Mount

A container tmpfs mount provides an in-memory filesystem at a selected container path. Its contents are not written into the image or the container's ordinary writable layer and disappear when the mount or host session ends.

This makes tmpfs useful for short-lived working data that should not persist, while size and permission options can limit how the process uses it. It is not a substitute for a [[Container Named Volume]] when data must survive removal, and sensitive content still needs process, swap, and host-access considerations despite avoiding ordinary disk persistence.

A Docker tmpfs mount stores data in host memory and never writes it into the image or durable volume. It fits temporary sensitive material and high-churn scratch data when loss at container stop or host restart is an intentional property.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
