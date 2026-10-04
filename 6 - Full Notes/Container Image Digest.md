2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Container Image Digest

A container image digest is a cryptographic identifier calculated from image content, commonly expressed with SHA-256. Manifests use digests to identify configurations and layers, and an image reference can use `@digest` to select a specific immutable manifest rather than a movable [[Container Image Tag]].

Digest verification detects changed or incorrectly transferred content and provides the stable identity needed for signing, policy, and reproducible deployment. It does not by itself establish who published the image; that provenance claim requires a trusted [[Container Image Signature]] and verification policy.

# References

[[podmanfordevopssecondedition.pdf]]
