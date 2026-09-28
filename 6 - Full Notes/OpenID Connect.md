2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# OpenID Connect

OpenID Connect is an authentication protocol built on OAuth 2.0 concepts. It lets a client application verify a user's identity through an identity provider and receive identity information in a standardized flow.

[[IdentityServer]] can expose OpenID Connect endpoints for an ASP.NET Core application. An Angular single-page client uses configured redirect and logout callbacks to participate in that flow.

In an Azure identity design, OpenID Connect provides interactive sign-in and identity claims, while OAuth 2.0 access tokens authorize calls to APIs. Keeping those purposes distinct prevents an ID token from being treated as an API credential. Conditional Access, multifactor requirements, application registrations, redirect URI validation, and secure token handling shape the complete sign-in flow around the protocol.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[azurecloudnativearchitecturemapbooksecondedition.pdf]]
