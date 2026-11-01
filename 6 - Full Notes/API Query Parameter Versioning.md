2026-10-31 21:16

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API Query Parameter Versioning

API query parameter versioning keeps the resource path stable and lets a client request a version through a value such as `/users?version=2`. Routing or application logic selects the corresponding contract from that parameter.

The method is easy to inspect and test but makes the query string carry a choice that affects the whole representation. The service must define a default, validate supported versions, and ensure caches and documentation distinguish responses that vary by the parameter.

# References

[[masteringrestapis.epub]]
