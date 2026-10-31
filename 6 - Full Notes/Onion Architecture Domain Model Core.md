2026-10-30 17:24

Status: #baby

Tags: [[Ports Adapters and Onion Architecture]]

# Onion Architecture Domain Model Core

The innermost onion layer contains domain entities and the logic intrinsic to their data. This model should depend on nothing outside the business domain, making it the most reusable and stable part of the application.

Controllers, transport formats, repository implementations, and external clients surround rather than define this core. Moving inward therefore removes technical context until only the application's business concepts and invariants remain.

# References

[[javamicroservicesandcontainersinthecloud.epub]]

