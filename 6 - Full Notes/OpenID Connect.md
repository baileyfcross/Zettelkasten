2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# OpenID Connect

OpenID Connect is an authentication protocol built on OAuth 2.0 concepts. It lets a client application verify a user's identity through an identity provider and receive identity information in a standardized flow.

[[IdentityServer]] can expose OpenID Connect endpoints for an ASP.NET Core application. An Angular single-page client uses configured redirect and logout callbacks to participate in that flow.

In an Azure identity design, OpenID Connect provides interactive sign-in and identity claims, while OAuth 2.0 access tokens authorize calls to APIs. Keeping those purposes distinct prevents an ID token from being treated as an API credential. Conditional Access, multifactor requirements, application registrations, redirect URI validation, and secure token handling shape the complete sign-in flow around the protocol.

Standardized in 2014, OpenID Connect adds an identity layer with provider discovery, identity claims, session-related behavior, and the ability to protect identity information within the surrounding OAuth flow. A social login must validate the returned ID token and correlate the response with the initiated request before mapping its subject to a local account. The ID token tells the client about an authentication event; an OAuth access token remains the credential intended for a protected API.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
