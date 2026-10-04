2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Writable Layer

A container writable layer is the thin, mutable filesystem layer placed above an image's read-only layers when a container is created. Copy-on-write behavior records additions and changes there while the shared image content remains unchanged.

The layer belongs to that container and normally disappears when the container is removed. It is appropriate for transient runtime changes, caches, and temporary files, but not for durable application data. Persistence should cross the container boundary through a [[Container Named Volume]] or [[Container Bind Mount]], while deliberate filesystem changes should normally be reproduced through an image build.

# References

[[podmanfordevopssecondedition.pdf]]
