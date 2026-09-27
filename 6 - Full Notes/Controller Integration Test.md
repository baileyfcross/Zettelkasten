2026-09-27 11:07

Status: #baby

Tags: [[ASP.NET Core API Integration Testing]]

# Controller Integration Test

A controller integration test exercises an ASP.NET Core controller together with routing, binding, filters, serialization, and its configured service dependencies. It sends an HTTP request to the application rather than calling the action method directly.

This scope detects mistakes that an isolated controller unit test cannot see, such as an incorrect route template, missing service registration, unexpected formatter behavior, or the wrong HTTP result mapping.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
