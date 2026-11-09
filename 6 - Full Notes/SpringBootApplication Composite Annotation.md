2026-11-08 16:45

Status: #baby

Tags: [[Spring Boot Configuration and Extensibility]]

# SpringBootApplication Composite Annotation

`@SpringBootApplication` combines three roles at the application boundary. `@SpringBootConfiguration` marks a source of bean definitions, `@ComponentScan` discovers components beneath the application's package, and `@EnableAutoConfiguration` asks Boot to contribute infrastructure that matches the available dependencies and current bean registry.

The combination explains why a thin main class can start a complete service. Component scanning registers application controllers and repositories, while auto-configuration supplies facilities such as the embedded server, DispatcherServlet, and message converters. Package placement therefore matters: types outside the scan root are not discovered unless scanning or imports are extended explicitly.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
