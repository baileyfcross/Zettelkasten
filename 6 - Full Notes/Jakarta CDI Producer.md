2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Producer

A Jakarta CDI producer turns a method return value or field value into a bean that the container can inject. Producers are useful for third-party classes, runtime-selected values, or objects that require construction logic outside an ordinary bean constructor. A producer may declare a scope and qualifiers for the object it supplies.

Producer method parameters are themselves injection points, and an InjectionPoint parameter can reveal metadata about the requesting location. A producer is a source of injectable objects rather than an injection target, so the producer method or field itself is not annotated with Inject; dependencies belong on its containing bean or among the method parameters.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
