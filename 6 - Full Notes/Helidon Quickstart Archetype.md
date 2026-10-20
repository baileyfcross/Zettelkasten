2026-10-19 22:48

Status: #baby

Tags: [[Helidon Platform Models and Project Tooling]]

# Helidon Quickstart Archetype

A Helidon Quickstart is a Maven archetype that generates a complete small REST application for either the SE or MP programming model. The generated greeting example includes `/greet` and `/simple-greet` endpoints, build configuration, source and test trees, application configuration, logging settings, and deployment assets.

The archetype coordinates group, artifact, package, and Helidon-version parameters so a project can be built with `mvn clean package` and started as a JAR. SE and MP use different archetype identifiers and Java source arrangements even though their example behavior is similar.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
