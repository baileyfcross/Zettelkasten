2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# OAuth Scope

An OAuth scope names a permission or access boundary a client may request for a resource. Scopes help limit a token to the part of a service the client actually needs rather than granting undifferentiated authority.

The book's IdentityServer configuration associates its client with the protected API scope before requesting a token. Application-specific role checks can further narrow individual operations after the token has established access to the resource.

# References

[[c8andnetcore30projectsusingazure.pdf]]
