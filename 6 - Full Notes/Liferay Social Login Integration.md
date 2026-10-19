2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Portals and Publishing]]

# Liferay Social Login Integration

Liferay can allow a portal user to sign in through a configured external identity or social provider. The portal participates in the provider flow, receives an identity assertion, and connects the external account to a portal user according to its account and matching rules.

This reduces another password interaction but introduces identity-linking risk. Email or profile similarity alone may not be sufficient proof that an existing portal account and an external account belong together, and provider access should not imply broad portal roles. Administrators must configure credentials, callback locations, requested data, and account creation policy carefully. The result brings [[OpenID Federated Identity Flow]] into the governed environment described by [[Liferay Portal Social Model]].

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
