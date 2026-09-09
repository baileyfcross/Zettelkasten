2026-09-08 22:09

Status: #baby

Tags: [[OAuth 2.0 and IdentityServer]]

# Role-Based Authorization

Role-based authorization grants or denies an operation according to a role associated with the authenticated user. It allows two users who can both enter an application to receive different capabilities.

The stock checker separates read and update permissions so staff roles can expose only the operations each job requires. Server enforcement protects the API, while matching UI changes avoid presenting controls that the current user cannot successfully invoke.

# References

[[c8andnetcore30projectsusingazure.pdf]]
