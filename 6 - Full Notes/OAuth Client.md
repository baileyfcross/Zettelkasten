2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# OAuth Client

An OAuth client is the application requesting an access token so it can call a protected resource. IdentityServer configuration identifies the client, its allowed grant, credentials, and the scopes or API resources it may request.

In the stock checker, the UWP application is the client and the ASP.NET Core API is the resource. Defining the client in the authorization server makes its permitted path to a token an explicit part of the system's trust model.

# References

[[c8andnetcore30projectsusingazure.pdf]]
