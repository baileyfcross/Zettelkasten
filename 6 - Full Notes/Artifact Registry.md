2026-10-03 22:25

Status: #baby

Tags: [[Platform Delivery and Artifact Automation]]

# Artifact Registry

An artifact registry stores and distributes versioned software assets such as container images, Helm charts, manifest bundles, and other OCI-compatible packages. In a platform it is an entry point between build and deployment, not passive storage.

The registry can enforce access control, replicate artifacts, record audit activity, scan vulnerabilities, apply retention or immutability rules, and emit lifecycle notifications. Because every deployable asset can pass through it, the registry is a strong policy checkpoint and evidence source, but also a critical service whose availability, integrity, and recovery requirements must be designed explicitly.

# References

[[platformengineeringforarchitects.pdf]]
