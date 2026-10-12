2026-10-04 08:37

Status: #baby

Tags: [[Podman Runtime Architecture and Isolation]]

# OCI Image Specification

The OCI Image Specification defines a portable, content-addressed format for container images. A manifest identifies a configuration object and ordered filesystem layers by media type, size, and digest; an optional image index can point to several manifests, commonly for different operating systems or processor architectures.

An OCI image layout stores these descriptors, manifests, configurations, and blobs in a standard directory structure. Because objects are identified by cryptographic digests and layers are immutable, tools can verify content and move it among registries, archives, and local stores without depending on the engine that built it.

# References

[[podmanfordevopssecondedition.pdf]]
