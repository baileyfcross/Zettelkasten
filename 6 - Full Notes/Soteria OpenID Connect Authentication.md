2026-10-18 22:56

Status: #baby

Tags: [[Java Social Authentication Frameworks]]

# Soteria OpenID Connect Authentication

A Jakarta application can implement OpenID Connect login as an HTTP authentication mechanism in Soteria. The mechanism redirects the user to the provider, handles the authorization response, exchanges and validates the resulting tokens, and establishes a caller identity that the container can expose to the application.

The integration must preserve the protocol's security checks rather than treating a successful redirect as authentication. State and nonce values bind the response to the initiated flow, redirect URIs must match, and token signatures and claims require validation. Once accepted, the external identity must still be mapped to local groups and roles. This joins [[OpenID Connect]] to [[Eclipse Soteria Authentication]] without collapsing authentication into authorization.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
