2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# Forwarded Headers Middleware

Forwarded Headers Middleware lets an ASP.NET Core application recover original request details supplied by a trusted reverse proxy, such as the client-facing scheme or address. Without it, the application sees only the proxy's connection to Kestrel.

The middleware must run early enough for later redirects and request handling to use the corrected values. Its trust settings should match the actual proxy arrangement.

# References

[[aspnetcore3andangular9_3ed.pdf]]
