2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Local Container Registry

A local container registry runs a distribution service within infrastructure controlled by the operator. A containerized registry can expose a port, store blobs in a persistent volume, require authentication, use TLS, permit deletion, and receive images copied or synchronized from other locations.

It is useful for laboratories, private networks, caching, and disconnected operation, but proximity does not make it trustworthy by itself. Persistent storage, backup, certificates, credentials, repository policy, and [[Container Registry Garbage Collection]] must be designed just as deliberately as for an externally hosted service.

# References

[[podmanfordevopssecondedition.pdf]]
