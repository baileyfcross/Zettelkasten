2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Skopeo Image Copy

Skopeo image copy transfers an image directly between supported transports, such as two registries, local container storage and a registry, a registry and an OCI layout, or archive and directory formats. Source and destination names explicitly identify their transports.

Unlike a pull followed by a push, the operation need not retain the image in the engine's ordinary local store. Separate source and destination credentials, authentication files, and TLS settings allow a pipeline to control both ends, while the copied manifests and blobs remain verifiable through their [[Container Image Digest]] values.

# References

[[podmanfordevopssecondedition.pdf]]
