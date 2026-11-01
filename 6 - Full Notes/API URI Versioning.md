2026-10-31 21:16

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API URI Versioning

API URI versioning places a version identifier in the resource path, such as `/v1/users` and `/v2/users`. The version is immediately visible in requests, routing rules, logs, links, and documentation.

The approach gives incompatible contracts distinct addresses, but it also makes the version part of every published URI. The book presents it as a clear strategy when the service is willing to preserve or redirect older version paths during a consumer transition.

# References

[[masteringrestapis.epub]]
