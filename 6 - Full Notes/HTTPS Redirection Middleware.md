2026-09-27 11:15

Status: #baby

Tags: [[ASP.NET Core API Security and Caching]]

# HTTPS Redirection Middleware

ASP.NET Core HTTPS redirection middleware answers an insecure HTTP request with a redirect to the corresponding HTTPS endpoint. Placing it early in the request pipeline prevents later application behavior from serving the protected resource over plaintext transport.

The middleware requires the application or its hosting environment to know the HTTPS port. When a reverse proxy terminates TLS, forwarded-header and proxy configuration must preserve the original scheme so redirects are accurate.

# References

[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
