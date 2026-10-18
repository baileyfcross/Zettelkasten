2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]] [[ASP.NET Core API Security and Caching]] [[Microservice Security and Observability]]

# Token-Based Authentication

Token-based authentication gives a client a token after successful authentication and requires that token on later protected requests. The server validates the token rather than retrieving all authentication state from a dedicated session.

The ASP.NET Core and Angular SPA flow uses a [[JSON Web Token]] issued through IdentityServer. An [[HTTP Interceptor]] can attach the token to outgoing client requests.

In a microservice system, an API gateway or individual service can validate a presented token before accepting a request, then apply role- or attribute-based authorization to the verified identity. The token avoids one shared server session but still requires protected signing keys, expiration, validation, and careful propagation. Authentication proves who or what presented the token; it does not by itself authorize every downstream operation.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[artofdecodingmicroservices.epub]]
