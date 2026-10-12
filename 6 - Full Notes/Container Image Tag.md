2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]] [[Docker Image Engineering]]

# Container Image Tag

A container image tag is a human-readable repository reference that points to an image manifest. Names such as `v1.0` or `latest` make selection convenient, but the registry can move a tag to a different manifest when a new image is pushed.

Tags are therefore mutable labels, not identity proofs. Deployment and promotion processes that require exact content should record a [[Container Image Digest]], while tags can continue to express a release channel or version name. Copying or retagging changes the reference without rewriting the underlying content-addressed layers.

A Docker image tag is a mutable human-readable reference that can be reassigned to a different manifest. Tags are convenient for release channels and discovery, but production promotion and policy checks should resolve or record the immutable digest behind the tag.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]

[[podmanfordevopssecondedition.pdf]]
