2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Qualifier

A Jakarta CDI qualifier is an annotation that narrows dependency resolution when more than one bean has a compatible Java type. The qualifier attached to an injection point must match the qualifier on the intended bean or producer, letting the container select a semantic role rather than relying on a concrete implementation class.

CDI supplies built-in qualifiers such as Default, Any, and Named and also permits application-specific qualifier annotations. The same mechanism can qualify produced objects and events, so one resolution vocabulary can distinguish implementations, select factories, and route notifications to matching observers.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
