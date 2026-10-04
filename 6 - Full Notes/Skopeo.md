2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Skopeo

Skopeo is a specialized command-line tool for examining and moving container images across registries, local container storage, OCI layouts, directories, and archive formats. It operates on image content without starting containers and often without first importing the image into the engine's local store.

Its commands include copy, inspect, list-tags, delete, login, digest calculation, signature operations, and synchronization. This makes Skopeo complementary to Podman and Buildah: Podman runs workloads, Buildah constructs images, and Skopeo performs distribution-oriented operations such as [[Skopeo Image Copy]] and [[Skopeo Registry Synchronization]].

# References

[[podmanfordevopssecondedition.pdf]]
