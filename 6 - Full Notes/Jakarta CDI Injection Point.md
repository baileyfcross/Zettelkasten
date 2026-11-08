2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Injection Point

A Jakarta CDI injection point is a location that requests a contextual instance from the container. CDI supports injected fields, constructor parameters, and initializer-method parameters; parameters of producer and observer methods can also be supplied by the container even without an explicit Inject annotation on each parameter.

The requested type and its qualifiers form the core resolution information. CDI also exposes InjectionPoint metadata to producer methods, allowing a producer to inspect where a value is being requested—for example, to create a logger named for the class that owns the injection point.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
