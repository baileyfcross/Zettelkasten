2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Container Image Signature

A container image signature binds a cryptographic signing claim to an image's immutable digest. Verification can show that the content being pulled is the content accepted by a particular signing key or identity, preventing a movable tag or intercepted registry path from silently substituting another manifest.

The signature is useful only when a [[Container Image Trust Policy]] specifies which identities and repositories are acceptable and fails closed when verification does not succeed. The image digest protects content integrity, while the trusted signature adds publisher authentication under the chosen key-management model.

# References

[[podmanfordevopssecondedition.pdf]]
