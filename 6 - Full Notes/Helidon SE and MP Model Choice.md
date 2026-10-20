2026-10-19 22:48

Status: #baby

Tags: [[Helidon Platform Models and Project Tooling]]

# Helidon SE and MP Model Choice

The Helidon model choice determines how an application expresses the same kinds of microservice concerns. [[Helidon SE Programming Model]] favors explicit builders, functional handlers, a tiny footprint, and no dependency-injection or enterprise-standards layer; [[Helidon MP Programming Model]] favors annotations, CDI-managed objects, and MicroProfile portability.

The distinction also affects project structure and implementation style. An SE greeting service implements Helidon interfaces and registers handlers in code, whereas an MP resource declares paths, HTTP verbs, scope, and injected configuration through annotations. Both remain standalone applications on the Helidon runtime.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
