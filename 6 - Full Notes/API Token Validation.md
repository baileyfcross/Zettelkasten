2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# API Token Validation

API token validation checks a presented access token before a protected controller action runs. The API is configured with an authentication scheme, the IdentityServer authority, and the resource name it expects the token to represent.

An authorization attribute then marks the controller or operation as protected. The client sets a bearer token on its HTTP calls, and requests without an acceptable token are rejected before business logic is trusted to execute.

# References

[[c8andnetcore30projectsusingazure.pdf]]
