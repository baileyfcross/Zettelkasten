2026-10-11 21:26

Status: #baby

Tags: [[Docker Networking and Compose]]

# Docker Compose Include

Docker Compose include assembles one project from separate Compose files, allowing service definitions to remain close to the code or team that owns them. Each included file is evaluated relative to its own project directory, so build contexts, volume paths, and environment-file references retain local meaning.

Include differs from an override: it imports distinct definitions rather than modifying fields of the same service. Names still share the resulting project namespace, so conflicts must be resolved explicitly and the combined application should be validated as one dependency and network graph.

# References

[[ultimatedockercontainerbookfourthedition.pdf]]
