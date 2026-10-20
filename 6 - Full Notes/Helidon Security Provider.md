2026-10-19 22:48

Status: #baby

Tags: [[Helidon Security Integration]]

# Helidon Security Provider

A Helidon security provider implements a particular authentication, authorization, assertion, or identity-integration mechanism behind the common security runtime. Available provider choices include HTTP Basic and Digest authentication, HTTP signatures, attribute-based access control, JWT, header assertion, Google login, OpenID Connect, and IDCS role mapping.

The provider is selected and configured independently of individual endpoint handlers. This lets a server path express that authentication or a role is required while the security configuration determines which mechanism establishes that identity.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
