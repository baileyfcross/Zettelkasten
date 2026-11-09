2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# Spring Boot Profile-Specific Configuration

Spring profiles select configuration and beans for named runtime environments. When a profile is active, `application-{profile}.properties` or its YAML equivalent supplements and overrides the application's defaults, while `@Profile` can make a bean definition conditional on expressions such as `dev | test` or `!prod`.

Profiles are useful for differences such as an in-memory development database versus PostgreSQL or sample-data initialization outside production. They should describe coherent environments rather than become a hidden branching system for business behavior. The active profile and its overrides are inputs to [[Spring Boot Externalized Configuration]], so deployments need an explicit and testable selection.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
