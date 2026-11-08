2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut Secured Controller

A Micronaut controller can use Secured to state the authentication or role rule required before its route executes. The book marks a controller with the authenticated-user rule and accepts a Principal parameter so the handler can read the identity established by Micronaut Security.

This keeps access policy at the HTTP entry point while the authentication provider remains responsible for establishing identity. A successful credential check and an authorization rule are separate decisions: authentication supplies the principal, and the controller's security rule determines whether that principal may invoke the route.

# References

[[prorestfulapiswithmicronaut.epub]]
