2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut JAX-RS Security Context Bridge

The ordinary SecurityContext supplied by Micronaut JAX-RS is not automatically aware of Micronaut Security roles. Without the security integration module, a resource that asks whether the current user has a role receives false even when Micronaut Security has authenticated the caller.

Adding the JAX-RS server security integration bridges SecurityContext.isUserInRole to the roles carried by Micronaut Security's Authentication object. This makes the compatibility API reflect the framework's authenticated identity instead of leaving two unrelated security views inside one request.

# References

[[prorestfulapiswithmicronaut.epub]]
