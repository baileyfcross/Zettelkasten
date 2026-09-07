2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# Reverse Proxy

A reverse proxy accepts client traffic on behalf of an application server and forwards requests to that server. It provides the public HTTP and HTTPS boundary while the application can listen on an internal address.

In the Linux deployment, [[Nginx]] proxies requests to [[Kestrel]]. Because the connection seen by Kestrel originates at the proxy, [[Forwarded Headers Middleware]] restores information about the original client request.

# References

[[aspnetcore3andangular9_3ed.pdf]]
