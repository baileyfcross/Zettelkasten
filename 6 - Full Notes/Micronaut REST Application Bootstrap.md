2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut REST Application Bootstrap

A Micronaut REST application begins from an ordinary Java main class that passes the application class to Micronaut.run. The framework starts its application context and HTTP runtime, after which discovered controllers can receive requests.

The generated project separates this bootstrap class from controllers, domain objects, services, and repositories. That boundary keeps application startup small while letting HTTP behavior grow through managed components rather than accumulating inside the main method.

# References

[[prorestfulapiswithmicronaut.epub]]
