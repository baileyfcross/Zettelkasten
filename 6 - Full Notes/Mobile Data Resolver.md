2026-09-22 23:04

Status: #baby

Tags: [[Mobile Data Synchronization and Notifications]]

# Mobile Data Resolver

A mobile data resolver expands compact identifiers in a transferred object into richer reference data held locally. Stable lookup information can be cached once, while frequently transferred records carry only its identifier, reducing repeated payload size.

Resolution belongs between transport and presentation so a view model receives usable objects without knowing whether details came from the network or local storage. Missing and stale reference entries require a fallback retrieval policy.

# References

[[hands-onmobiledevelopmentwithnetcore.pdf]]
