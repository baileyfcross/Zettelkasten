2026-10-31 21:16

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API URI Versioning

API URI versioning places a version identifier in the resource path, such as `/v1/users` and `/v2/users`. The version is immediately visible in requests, routing rules, logs, links, and documentation.

The approach gives incompatible contracts distinct addresses, but it also makes the version part of every published URI. The book presents it as a clear strategy when the service is willing to preserve or redirect older version paths during a consumer transition.

The Micronaut source recommends a mandatory, leftmost path segment with a `v` prefix and a whole ordinal such as `/v1`, avoiding decimal notation that suggests implementation-level granularity. It also treats transition support as part of publication: retain at least one prior version and give consumers a release cycle to adapt before obsoleting it.

The Spring Boot example maps legacy and modern customer contracts to distinct controllers and repositories. The older path continues accepting its permissive representation while the newer path adds a field and Jakarta validation, and one test demonstrates both behaviors. This shows that version routing preserves executable behavior, not merely two URLs pointing at the same implementation.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[masteringrestapis.epub]]

[[prorestfulapiswithmicronaut.epub]]
