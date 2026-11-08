2026-11-08 14:08

Status: #baby

Tags: [[Jakarta CDI Dependency Management]]

# Jakarta CDI Contextual Scope

A Jakarta CDI scope defines the context in which a contextual instance exists and can be reused. Application scope associates one instance with the running application; request scope associates instances with an individual servlet, REST, remote EJB, or asynchronous-observer dispatch; session and conversation scopes retain state across longer web interactions; dependent scope ties an object's lifecycle to the object into which it is injected.

Scope is therefore a lifecycle and sharing decision, not merely an annotation. The container creates the appropriate context, selects or creates an instance within it, and destroys scoped instances when that context ends. Longer-lived scopes can share more state but also require stronger attention to concurrency and passivation constraints.

# References

[[procloud-nativejavaeeapps_devopswithmicroprofilejakartaee11apisand.epub]]
