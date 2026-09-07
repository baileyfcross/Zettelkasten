2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# Token-Based Authentication

Token-based authentication gives a client a token after successful authentication and requires that token on later protected requests. The server validates the token rather than retrieving all authentication state from a dedicated session.

The ASP.NET Core and Angular SPA flow uses a [[JSON Web Token]] issued through IdentityServer. An [[HTTP Interceptor]] can attach the token to outgoing client requests.

# References

[[aspnetcore3andangular9_3ed.pdf]]
