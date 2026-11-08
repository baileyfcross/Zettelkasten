2026-11-08 16:00

Status: #baby

Tags: [[Micronaut REST Application Framework]]

# Micronaut Authentication Provider

A Micronaut authentication provider receives an authentication request and returns either a successful authenticated identity or a failure reason. Registering the provider as a managed singleton lets Micronaut Security invoke it when an HTTP authentication mechanism supplies credentials.

The book's deliberately simple provider compares a submitted identity and secret with fixed values to demonstrate the extension point. A real provider should move credential verification to an appropriate identity store and should not embed reusable secrets in application code.

# References

[[prorestfulapiswithmicronaut.epub]]
