2026-11-08 16:45

Status: #baby

Tags: [[Spring Cloud Operations and Native Runtime]]

# Spring Boot Actuator Endpoint Security

Spring Boot Actuator exposes operational endpoints for health, information, metrics, environment, bean inspection, log levels, thread dumps, and custom management operations over HTTP or JMX. Exposure and authorization should be narrower than the set of endpoints available in the application.

A security matcher can permit health and selected information to unauthenticated load balancers while requiring an administrative role for sensitive endpoints such as environment or bean details. Exposure, network reachability, and authorization are separate controls. A custom endpoint's read or delete operation must be treated as an operational API, especially when it can clear state or change behavior.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
