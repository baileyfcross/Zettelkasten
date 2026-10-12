2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]] [[TLS Authentication and Secure Remote Access]]

# OAuth 2.0

OAuth 2.0 is an authorization framework in which a client obtains an access token for a protected resource instead of sending a user's credentials with every API request. The participants and grant define how that token is requested and what it can be used to access.

The stock-checker project uses IdentityServer 4 to issue a token to a UWP client and configures an ASP.NET Core API to validate it. Authentication establishes the user, while role-sensitive authorization still decides whether that user may read or update stock.

The Azure architecture map places OAuth 2.0 access tokens at the API boundary, where an API gateway can validate issuer, audience, claims, scopes, and expiry before routing a request. Token validation authenticates the presented authorization grant; the backend must still enforce resource-level permissions and tenant boundaries. Managed identities complement rather than replace this model by authenticating Azure workloads to downstream services without user credentials.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
