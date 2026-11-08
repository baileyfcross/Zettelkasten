2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# OAuth Grant Type

An OAuth grant type defines the interaction through which a client obtains authorization and an access token. It identifies which participant supplies credentials, what trust the client receives, and whether user interaction occurs at the authorization server.

Grant selection is a security and usability decision rather than a interchangeable configuration label. The book examines the limitations of its [[Resource Owner Password Grant]] and notes that a server-hosted login can keep sensitive authentication logic out of desktop code.

The Micronaut book surveys authorization code, implicit, resource-owner password credentials, and client credentials flows. Authorization code keeps the access-token exchange on a server-side client; implicit exposes a token to browser code and is described as the least secure option; the password flow requires exceptional trust because the client receives user credentials; and client credentials represents machine access without an end-user authorization step.

# References

[[c8andnetcore30projectsusingazure.pdf]]

[[prorestfulapiswithmicronaut.epub]]
