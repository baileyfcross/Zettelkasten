2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# Spring Boot Enable Annotation Pattern

The Spring `@Enable...` pattern creates a domain-specific annotation that imports the configuration needed for a feature. A consuming application places that annotation on a configuration class or its Boot entry point, making the decision to activate the feature visible in source.

The imported configuration can still use properties and conditions, so explicit enablement does not require unconditional bean creation. This pattern is useful when classpath presence alone should not turn on behavior, or when a custom starter offers both automatic and deliberate activation paths.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
