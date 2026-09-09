2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]] [[OAuth 2.0 and IdentityServer]]

# IdentityServer

IdentityServer is middleware that adds OpenID Connect and OAuth 2.0 endpoints to an ASP.NET Core application. It connects the application's identity records to clients that need tokens and standardized authentication flows.

An SPA profile defines defaults such as login and logout callback locations, allowed response types, and scopes. Development signing settings should remain environment-specific rather than being copied into production configuration.

The stock-checker project presents IdentityServer 4 as a framework for running an identity service rather than a prebuilt external provider. Its configuration identifies users, protected API resources, and clients, then supplies signing credentials so issued tokens can be trusted by the API.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
