2026-10-04 08:37

Status: #baby

Tags: [[Rootless Container and SELinux Security]]

# Rekor Transparency Log

Rekor is an append-oriented transparency log for recording signed software-supply-chain events. When a container-image signature is entered, the log gives independent observers an auditable record that can be searched and checked rather than leaving every verification claim inside one private registry or pipeline.

The record strengthens accountability and makes later denial or quiet replacement more difficult, but transparency does not decide whether a signer should be trusted. A consumer still needs a [[Container Image Trust Policy]] and an identity or key policy appropriate to the repository and release process.

# References

[[podmanfordevopssecondedition.pdf]]
