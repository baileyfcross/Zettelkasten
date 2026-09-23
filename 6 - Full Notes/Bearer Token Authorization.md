2026-09-22 23:34

Status: #baby

Tags: [[TLS Authentication and Secure Remote Access]]

# Bearer Token Authorization

Bearer token authorization grants access to whoever presents a valid token in the HTTP `Authorization` header. The resource server validates the token rather than requiring the user's password on every request.

Because possession is sufficient, a bearer token must be protected in storage and transit. Its scope and lifetime should limit the damage if it is disclosed, and TLS prevents passive observers from reading it on the wire.

# References

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]
