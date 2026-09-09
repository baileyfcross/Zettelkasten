2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# Resource Owner Password Grant

The resource owner password grant sends a user's username and password from a trusted client to the authorization service in exchange for an access token. The book uses it for a constrained 2019 desktop application that must work with a locally hosted identity service.

The flow makes the client responsible for collecting credentials and can expose an embedded client secret through reverse engineering. The chapter therefore treats it as a tradeoff for its offline-oriented scenario and points toward a hosted authentication interface as a safer design for broader access.

# References

[[c8andnetcore30projectsusingazure.pdf]]
