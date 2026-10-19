2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Identity Security]]

# OpenID Federated Identity Flow

OpenID allows a relying application to accept an identity assertion from an external provider rather than creating another site-specific credential. The user chooses or is directed to a provider, authenticates there, and returns to the relying party with a response that the application must verify before establishing its local session.

Federation reduces repeated password handling but transfers important trust decisions to the provider relationship and protocol validation. The application must verify the response, bind it to the initiated request, and decide how the external identity maps to a local account and permissions. Modern social login commonly uses [[OpenID Connect]], which places identity claims on OAuth-based flows; it should not be confused with granting API access through [[OAuth 2.0]].

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
