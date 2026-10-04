2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Sigstore Image Signing

Sigstore image signing records a signature for a digest-addressed container image so clients can verify it before use. Podman and Skopeo can create and consume Sigstore-style signatures, while Cosign provides another signing workflow and [[Rekor Transparency Log]] can publish auditable signing events.

Signing should occur after the final image content is known, ideally in a controlled build or promotion pipeline. Verification must be tested with altered or unsigned content; generating a signature without configuring enforcement leaves the consumer free to pull an untrusted image.

# References

[[podmanfordevopssecondedition.pdf]]
