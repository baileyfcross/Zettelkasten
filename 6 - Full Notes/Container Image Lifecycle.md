2026-10-04 08:37

Status: #baby

Tags: [[Podman Container Lifecycle and Storage]]

# Container Image Lifecycle

The container image lifecycle covers discovering, pulling, inspecting, tagging, using, and removing immutable image content. Podman searches configured registries, downloads missing manifests and layers into local storage, and creates containers from that cached content without changing the original layers.

Images and containers therefore have related but different lifecycles. An image can remain after every container created from it has been removed, and several containers can share its read-only layers while each receives a separate [[Container Writable Layer]]. Pruning should target content that is genuinely unreferenced rather than treating every stopped container or old tag as the same object.

# References

[[podmanfordevopssecondedition.pdf]]
