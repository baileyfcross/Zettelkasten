2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Skopeo Remote Inspection

Skopeo remote inspection retrieves image metadata from a registry without pulling all of its layers into local container storage. The JSON result can reveal the repository name, digest, tags, creation data, architecture, operating system, labels, environment, and layer digests.

This supports a preflight decision about platform compatibility, provenance inputs, or available versions before transfer or execution. Authentication and TLS rules still apply, and metadata should be tied to a [[Container Image Digest]] when later automation must act on exactly the inspected content.

# References

[[podmanfordevopssecondedition.pdf]]
