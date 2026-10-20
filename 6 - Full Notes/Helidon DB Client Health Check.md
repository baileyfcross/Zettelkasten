2026-10-19 22:48

Status: #baby

Tags: [[Helidon Database Client]]

# Helidon DB Client Health Check

Helidon DB Client can register a database health-check service through `DbClientHealthCheck`. The utility implements the MicroProfile `HealthCheck` contract and executes a configured database check as part of application health reporting.

The MongoDB example defines a named `health-check` command that pings the database and identifies it as a query. This keeps the probe under the same configuration and client abstraction as ordinary statements while making database availability visible to [[Helidon Health Checks]].

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
