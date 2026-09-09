2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# OAuth 2.0

OAuth 2.0 is an authorization framework in which a client obtains an access token for a protected resource instead of sending a user's credentials with every API request. The participants and grant define how that token is requested and what it can be used to access.

The stock-checker project uses IdentityServer 4 to issue a token to a UWP client and configures an ASP.NET Core API to validate it. Authentication establishes the user, while role-sensitive authorization still decides whether that user may read or update stock.

# References

[[c8andnetcore30projectsusingazure.pdf]]
