2026-10-03 22:25

Status: #baby

Tags: [[Platform Security and Software Supply Chain]]

# Immutable Artifact Digest

An immutable artifact digest identifies the exact bytes of a build with a cryptographic hash. Deployment by digest ensures that the object validated, scanned, and approved is the same object retrieved later, even if a human-friendly version label is reused.

A mutable or floating tag such as `latest` can be redirected to different content without changing the deployment reference, weakening reproducibility and supply-chain evidence. Human versions remain useful for communication, but the platform should resolve them to digests for promotion, inventory, policy, and rollback. Signatures and attestations can then bind additional evidence to that stable identity.

# References

[[platformengineeringforarchitects.pdf]]
