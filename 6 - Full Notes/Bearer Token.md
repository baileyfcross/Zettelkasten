2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# Bearer Token

A bearer token authorizes whoever presents it, so possession of the token is sufficient for the protected server to consider the associated access claim. The stock-checker client places its token in the HTTP authorization header before calling the API.

Because the credential is usable by its bearer, it must be protected in transport and storage and limited to the intended resource and scope. The API validates it before the controller's protected operation is allowed to run.

# References

[[c8andnetcore30projectsusingazure.pdf]]
