2026-09-27 11:07

Status: #baby

Tags: [[ASP.NET Core API Integration Testing]]

# ASP.NET Core Integration Test Client

An ASP.NET Core integration-test client is the `HttpClient` produced by a test server or `WebApplicationFactory`. Its requests enter the application at the HTTP boundary, so status codes, headers, serialization, routing, and dependency wiring are observed together.

The client should use stable test data and explicit assertions about the response contract. This keeps the test focused on what an API consumer can observe instead of controller implementation details.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
