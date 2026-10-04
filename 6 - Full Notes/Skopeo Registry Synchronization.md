2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Skopeo Registry Synchronization

Skopeo registry synchronization copies selected images, tags, or whole repositories between a registry and another registry or directory. A YAML source can describe several repositories and tag-selection patterns, making the operation suitable for scheduled mirrors and disconnected environments.

The destination should preserve enough source scope to prevent repositories with the same short name from colliding. Synchronization is also a policy boundary: the mirror's refresh schedule, accepted sources, signatures, and retention determine whether isolated clients receive current and trusted content rather than merely a convenient copy.

# References

[[podmanfordevopssecondedition.pdf]]
