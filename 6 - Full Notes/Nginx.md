2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# Nginx

Nginx is a web server that can act as the public [[Reverse Proxy]] for a Linux-hosted ASP.NET Core application. It listens for HTTP or HTTPS traffic and passes application requests to a Kestrel service.

The Nginx configuration identifies the upstream address, certificate material, and forwarded request headers. Separating these responsibilities keeps Kestrel behind the public network boundary.

# References

[[aspnetcore3andangular9_3ed.pdf]]
