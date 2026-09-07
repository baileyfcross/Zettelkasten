2026-09-06 20:52

Status: #baby

Tags: [[Web Identity and Access Control]]

# Auth0

Auth0 is the external identity service configured in the book for the ASP.NET Core API and React client. It authenticates the user, issues tokens for the configured application and API, and exposes identity information to the client session.

The API still validates every presented token and applies its own authorization policy. Delegating identity management does not delegate the application's decisions about which protected operation a user may perform.

# References

[[aspnetcore3andreact.pdf]]
