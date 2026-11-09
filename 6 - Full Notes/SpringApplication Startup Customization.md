2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# SpringApplication Startup Customization

`SpringApplication` controls how a Spring Boot application is launched beyond the default static `run` call. Its builder can select the application type, attach listeners, change banner behavior, add initializers, and supply other startup choices before the application context is created.

Startup customization should remain at the composition boundary. Disabling a banner or registering a lifecycle listener changes how the process starts; it should not move feature behavior into the main class. Once initialization is complete, `ApplicationReadyEvent` provides a defined point for work that must wait until the context and server are ready.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
