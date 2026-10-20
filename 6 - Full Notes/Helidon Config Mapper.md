2026-10-19 22:48

Status: #baby

Tags: [[Helidon Configuration System]]

# Helidon Config Mapper

A Helidon config mapper converts a `Config` subtree into a specific Java type. Mapper providers supply ordered mapping functions so component or application code can consume a structured object instead of repeatedly reading individual string keys.

Helidon discovers `ConfigMapperProvider` implementations through Java `ServiceLoader` and registers their mappers with each builder by default. A builder can disable that automatic service loading when it needs an explicitly controlled mapper set.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
