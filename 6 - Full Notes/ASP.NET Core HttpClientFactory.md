2026-09-08 21:16

Status: #baby

Tags: [[ASP.NET Core Web API Development]]

# ASP.NET Core HttpClientFactory

`IHttpClientFactory` centralizes the creation and configuration of `HttpClient` instances in ASP.NET Core. It supports named or typed clients and manages underlying handlers so applications can reuse connections without treating one manually configured client as an unstructured global dependency.

Central configuration provides a natural place for base addresses, headers, logging, and resilience policies. Consumers receive a client through dependency injection, which makes their external-service dependency visible and easier to replace during tests.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
