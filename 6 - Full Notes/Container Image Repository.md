2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Container Image Repository

A container image repository is a named collection of related image manifests within a [[Container Registry]]. Tags in the repository usually identify releases or variants, while manifests and layers are stored as content-addressed objects that may be shared with other images.

The repository name forms part of a complete image reference together with the registry, optional namespace, and tag or digest. Access policy, mirroring, and retention can therefore be applied at repository or namespace scope rather than treating every image as an unrelated file.

# References

[[podmanfordevopssecondedition.pdf]]
