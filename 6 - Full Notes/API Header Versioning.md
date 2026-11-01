2026-10-31 21:16

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API Header Versioning

API header versioning asks the client to place the desired contract version in an HTTP request header. This keeps resource URIs free of version segments and allows routing middleware or controller conditions to select an implementation.

Because the version is less visible than a path segment, clients need precise documentation and diagnostic output. Intermediary caches must also vary on the relevant header when different versions can share the same URI.

# References

[[masteringrestapis.epub]]
