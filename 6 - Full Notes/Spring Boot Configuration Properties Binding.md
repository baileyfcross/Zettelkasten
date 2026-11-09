2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# Spring Boot Configuration Properties Binding

`@ConfigurationProperties` maps a named configuration prefix into a Java class or record, turning a group of external values into one typed dependency. `@ConfigurationPropertiesScan` discovers those types and registers them as beans, allowing a service to depend on a settings object rather than scattering individual `@Value` expressions through its code.

Relaxed binding recognizes common spelling variants such as kebab case, underscore form, and conventional property names. Prefixes keep unrelated settings apart, and type conversion makes an invalid value visible during binding instead of after a distant use. This gives [[Spring Boot Externalized Configuration]] a reviewable application-facing contract.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
