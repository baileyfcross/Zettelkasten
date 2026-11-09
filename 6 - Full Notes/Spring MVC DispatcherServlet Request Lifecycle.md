2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring MVC DispatcherServlet Request Lifecycle

The Spring MVC `DispatcherServlet` is the front controller for servlet requests. It asks a handler mapping to select a controller method, uses a handler adapter to resolve arguments and invoke that method, and passes a REST return value to an HTTP message converter before writing the response.

Annotations participate at different stages of this pipeline. Request mappings register candidate handlers at startup, path variables and request bodies guide argument resolution, and `@RestController` makes the result a response body rather than a view name. Seeing the stages separately helps locate a failure in routing, binding, validation, controller logic, or serialization instead of treating the entire exchange as controller behavior.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
