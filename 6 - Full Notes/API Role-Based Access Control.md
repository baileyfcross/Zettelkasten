2026-10-31 21:16

Status: #baby

Tags: [[REST API Security and Access Control]]

# API Role-Based Access Control

API role-based access control assigns authenticated users or clients to roles and maps each role to permitted operations. Middleware, policies, or controller annotations reject a request when the validated identity lacks the required role.

The book uses roles such as administrator, user, and guest to separate resource access. Role mapping occurs after authentication, and a 403 response represents a known subject that is not authorized for the requested action. Resource-specific conditions can extend the broad role decision.

# References

[[masteringrestapis.epub]]
