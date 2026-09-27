2026-09-27 10:58

Status: #baby

Tags: [[ASP.NET Core Request Pipeline Customization]]

# HttpContext in ASP.NET Core

`HttpContext` represents the current ASP.NET Core HTTP exchange. It exposes the request, response, connection, user, services, and per-request items that middleware and endpoint code use while handling that exchange.

The context belongs to one active request and should not be treated as durable application state. Components can enrich it for later pipeline stages, but business logic is easier to test when it receives explicit values instead of depending directly on the entire context.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
