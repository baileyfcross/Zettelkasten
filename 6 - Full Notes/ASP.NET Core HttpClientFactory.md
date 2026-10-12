2026-09-08 21:16

Status: #baby

Tags: [[ASP.NET Core Web API Development]] [[.NET Network Requests Sockets and Streams]] [[.NET Microservice Communication and Workers]]

# ASP.NET Core HttpClientFactory

`IHttpClientFactory` centralizes the creation and configuration of `HttpClient` instances in ASP.NET Core. It supports named or typed clients and manages underlying handlers so applications can reuse connections without treating one manually configured client as an unstructured global dependency.

Central configuration provides a natural place for base addresses, headers, logging, and resilience policies. Consumers receive a client through dependency injection, which makes their external-service dependency visible and easier to replace during tests.

The architecture book uses the factory to create efficient outbound REST clients without repeatedly constructing unmanaged handler resources. Typed or named configuration keeps remote-service addresses and behavior outside controllers.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
