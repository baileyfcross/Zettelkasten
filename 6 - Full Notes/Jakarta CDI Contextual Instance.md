2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Contextual Instance

A Jakarta CDI bean is a source or blueprint for objects, while a contextual instance is an object the container creates from that bean to satisfy a dependency. The container, rather than application code, performs creation and destruction through the bean's contextual contract.

Every contextual instance belongs to a context governed by a scope. When an injection point requests a bean, the container must return the instance appropriate to the active context, creating one when the scope requires it and reusing or destroying it according to that scope's lifecycle.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
