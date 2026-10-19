2026-10-18 22:56

Status: #baby

Tags: [[Java Social Authentication Frameworks]]

# Keycloak Realm and Client Model

A Keycloak realm is an administrative and security boundary containing users, credentials, roles, groups, and identity-provider relationships. A client represents an application or service that relies on the realm for authentication or delegated access.

Client configuration defines details such as protocol, redirect destinations, credentials, and permitted flows. Roles may apply across the realm or belong to a particular client, which lets a shared identity remain subject to application-specific authority. Separating production, test, or organizational populations into appropriate realms can reduce accidental trust expansion. These boundaries operationalize [[Keycloak Identity and Access Management]]: the realm defines the identity domain, the client defines the relying application, and mappings determine what external social identities become locally.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
