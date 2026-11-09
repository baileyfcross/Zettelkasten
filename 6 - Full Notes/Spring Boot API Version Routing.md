2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring Boot API Version Routing

Spring Boot API version routing can give incompatible contracts distinct request mappings, such as separate versioned path prefixes. Each controller can bind its own representation, repository, and validation policy, allowing a permissive legacy endpoint to remain available while a stricter version is introduced.

The explicit controller split complements [[API URI Versioning]] by keeping behavior as well as the address separate. It avoids condition-heavy methods that silently vary by client, but it also means both versions must be tested and retired deliberately. A version is therefore a supported contract and migration period, not merely a number embedded in a route.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
