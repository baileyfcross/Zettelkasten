2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Security Construction Modes

Helidon Security can be assembled in three ways: a builder can receive security settings programmatically, a configuration file can define them, or an application can combine both approaches. The `Security.create(Config)` path creates the runtime directly from configuration values.

These modes separate the location of policy from the policy's meaning. Builder construction makes composition explicit in Java, file-based construction makes deployment changes external, and the hybrid form keeps fixed integration code while leaving environment-specific providers or rules configurable.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
