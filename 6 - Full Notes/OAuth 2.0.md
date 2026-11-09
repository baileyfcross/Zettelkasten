2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]] [[TLS Authentication and Secure Remote Access]]

# OAuth 2.0

OAuth 2.0 is an authorization framework in which a client obtains an access token for a protected resource instead of sending a user's credentials with every API request. The participants and grant define how that token is requested and what it can be used to access.

The stock-checker project uses IdentityServer 4 to issue a token to a UWP client and configures an ASP.NET Core API to validate it. Authentication establishes the user, while role-sensitive authorization still decides whether that user may read or update stock.

The Azure architecture map places OAuth 2.0 access tokens at the API boundary, where an API gateway can validate issuer, audience, claims, scopes, and expiry before routing a request. Token validation authenticates the presented authorization grant; the backend must still enforce resource-level permissions and tenant boundaries. Managed identities complement rather than replace this model by authenticating Azure workloads to downstream services without user credentials.

For a social integration, OAuth lets a resource owner authorize a client to call a platform's resource server without giving the client the owner's password. The authorization grant and resulting access token are bounded by the provider, client registration, scopes, and lifetime. This makes narrow scope selection and token protection central: obtaining delegated access to one social capability does not grant general authority over the user's account or over the enterprise application's own resources.

In the book's microservice deployment, the API gateway acts as a confidential client in an authorization-code flow, the authorization server issues access tokens, and each service that owns protected resources can act as a resource server. Tokens can be propagated between services, but every recipient must still validate the token and enforce access to the resource it owns.

The Micronaut source separates the resource owner, client, authorization server, and resource server roles. A short-lived access token accompanies protected-resource requests, while an optional refresh token returns only to the authorization server to obtain a replacement access token. Client registration records redirect locations and permitted grants and returns a client identifier plus any secret the client is capable of protecting.

The Spring Security source applies these roles to a reactive resource server: a trusted authorization server authenticates the user and issues a JWT, and the service validates that token and maps its scopes into authorities. Mutual TLS can separately authenticate a confidential service client to the authorization server, demonstrating that OAuth authorization and connection-level workload identity solve different parts of the trust path.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[c8andnetcore30projectsusingazure.pdf]]

[[hands-onnetworkprogrammingwithcandnetcore.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
[[practicalmicroservicesarchitecturalpatterns.epub]]

[[prorestfulapiswithmicronaut.epub]]
