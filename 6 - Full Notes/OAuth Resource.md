2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# OAuth Resource

An OAuth resource is the protected service for which an access token is intended. The stock-checker API is registered as a resource, and its authentication middleware treats the IdentityServer authority as the issuer whose tokens it will validate.

A token meant for one resource should not be treated as general permission across every service. Resource configuration gives the authorization server and API a shared name for the boundary being protected.

# References

[[c8andnetcore30projectsusingazure.pdf]]
