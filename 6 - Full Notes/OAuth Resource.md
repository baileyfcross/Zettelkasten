2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# OAuth Resource

An OAuth resource is the protected service for which an access token is intended. The stock-checker API is registered as a resource, and its authentication middleware treats the IdentityServer authority as the issuer whose tokens it will validate.

A token meant for one resource should not be treated as general permission across every service. Resource configuration gives the authorization server and API a shared name for the boundary being protected.

The resource server hosts the protected data or operations and receives the access token from the client. Its role is distinct from the authorization server that issues the token, even when both roles run in one deployment. The resource server must validate the presented token and apply its local authorization rules before returning data.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[prorestfulapiswithmicronaut.epub]]
