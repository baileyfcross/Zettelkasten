2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Container Image Trust Policy

A container image trust policy tells the containers/image stack whether image content from a given transport and repository may be accepted and which signatures must verify. Rules can reject content by default, accept it without signature checks, or require a signature from an approved key or identity for a scoped source.

The policy turns [[Container Image Signature]] data into an enforceable pull decision. Its scope should match repository ownership and promotion boundaries, and failure tests should confirm that an unsigned image, wrong signer, changed digest, or mismatched repository is actually rejected rather than merely reported.

# References

[[podmanfordevopssecondedition.pdf]]
