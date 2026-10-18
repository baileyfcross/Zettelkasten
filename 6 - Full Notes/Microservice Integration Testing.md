2026-10-18 15:54

Status: #baby

Tags: [[Microservice Testing Deployment and Scaling]]

# Microservice Integration Testing

Microservice integration testing verifies that a service's internal components and selected external boundaries work together. It can exercise routing, serialization, persistence, framework configuration, or a controlled dependency with more realism than [[Microservice Unit Testing]].

The test should state which integration it owns so failures remain diagnosable. Replacing every dependency with a mock can miss configuration and protocol errors, while depending on an uncontrolled shared environment makes the test slow and unstable. Integration tests sit between isolated unit tests and [[Microservice End-to-End Testing]]: they provide concrete evidence at a boundary without requiring the entire distributed system to be running.

# References

[[artofdecodingmicroservices.epub]]
