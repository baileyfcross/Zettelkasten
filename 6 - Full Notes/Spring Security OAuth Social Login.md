2026-10-18 22:56

Status: #baby

Tags: [[Java Social Authentication Frameworks]]

# Spring Security OAuth Social Login

Spring Security can act as an OAuth 2.0 client and provide login through an OpenID Connect-capable identity provider. Client registration supplies the provider endpoints, identifier, secret, scopes, and redirect URI; the framework manages redirects and processes the authorization response.

The returned identity still requires application policy. Claims or provider attributes must be mapped deliberately to a local user and authorities, and an OAuth access token should be used only for its intended resource. The integration rests on the request processing described by [[Spring Security Provider and Filter Chains]]. It also preserves the distinction between [[OpenID Connect|identity authentication]] and [[OAuth 2.0|delegated API authorization]], even though one user journey may employ both.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
