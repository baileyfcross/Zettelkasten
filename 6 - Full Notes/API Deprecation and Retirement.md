2026-10-31 21:16

Status: #baby

Tags: [[REST API Versioning Documentation and Governance]]

# API Deprecation and Retirement

API deprecation announces that a contract remains available temporarily but should no longer be chosen for new integrations. Retirement is the later lifecycle event that removes or disables that version after its transition period.

The book recommends publishing the reason, replacement, migration instructions, schedule, and final retirement notice. Monitoring remaining usage helps the provider find active consumers before removal and prevents a nominal deadline from concealing unknown dependencies.

Within an API management lifecycle, a deprecated API can remain deployed for existing users while disappearing from discovery for new consumers. Retirement follows when the API is unpublished and removed. Version replacement, security concerns, technology changes, declining usage, or lost business value may motivate the transition, but none removes the need to communicate it to dependent clients.

# References

[[masteringrestapis.epub]]

[[prorestfulapiswithmicronaut.epub]]
