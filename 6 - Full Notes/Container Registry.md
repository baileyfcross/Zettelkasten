2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Container Registry

A container registry is a distribution service for image manifests, configurations, layers, signatures, and repository metadata. Engines and specialized clients use registry APIs to authenticate, discover content, pull blobs, and push new image references without transferring layers the registry already possesses.

Public, hosted private, and on-premises registries implement the same general distribution role but differ in access, availability, governance, and network reachability. A registry is not merely file storage: repository naming, authentication, TLS, retention, deletion, and [[Container Registry Garbage Collection]] all affect whether an image can be distributed safely.

# References

[[podmanfordevopssecondedition.pdf]]
