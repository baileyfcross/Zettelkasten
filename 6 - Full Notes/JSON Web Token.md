2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# JSON Web Token

A JSON Web Token is a compact token format used to carry signed claims between an issuer and a client or API. Its signature allows the recipient to detect alteration and validate the issuing authority.

In a single-page application, IdentityServer can issue a JWT after authentication and the client can present it on API requests. The token is evidence to validate, not permission by itself; [[Authorization]] still evaluates the claims against an operation's policy.

# References

[[aspnetcore3andangular9_3ed.pdf]]
