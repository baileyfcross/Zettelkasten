2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut Compile-Time Dependency Injection

Micronaut builds dependency-injection metadata while compiling an application rather than discovering and wiring the complete object graph through runtime reflection. The generated metadata lets its container resolve managed components with less startup work and a smaller runtime memory footprint.

Application classes still declare their required collaborators, commonly through constructors, while the container owns their creation and references. Moving metadata analysis to compilation does not remove dependency injection; it changes when the framework prepares the information needed to perform it.

# References

[[prorestfulapiswithmicronaut.epub]]
