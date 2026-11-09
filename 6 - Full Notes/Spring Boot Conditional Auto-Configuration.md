2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# Spring Boot Conditional Auto-Configuration

Spring Boot auto-configuration discovers candidate configuration classes from `META-INF/spring/org.springframework.boot.autoconfigure.AutoConfiguration.imports` files on the classpath. Conditions then decide whether each candidate should contribute beans by examining facts such as available classes, existing beans, configuration properties, and the type of application being started.

This creates convention with an escape hatch. A web starter can cause Boot to configure an embedded server and Spring MVC defaults, yet a user-provided bean makes the matching default back away. The decision is therefore a conditional composition process rather than an unconditional framework takeover, and the same model supports [[Spring Boot Conditional Starter Beans]] in organization-specific extensions.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
