2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Interceptor Binding

A Jakarta CDI interceptor binding is a type-safe annotation that associates a bean or method with cross-cutting behavior such as logging. The binding marks the target, while a separate interceptor class implements the behavior and is enabled and ordered independently of the target's business code.

An AroundInvoke interceptor method receives an invocation context, runs before or around the target call, and invokes proceed to continue through the remaining interceptor chain or reach the target method. This separates technical policy from business logic while retaining explicit, annotation-based attachment at the points where the policy applies.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
