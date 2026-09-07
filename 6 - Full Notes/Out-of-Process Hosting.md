2026-09-06 20:41

Status: #baby

Tags: [[Web Application Deployment]]

# Out-of-Process Hosting

Out-of-process hosting runs the ASP.NET Core application in a separate [[Kestrel]] process behind a public-facing server. The front server accepts the external connection and forwards matching traffic to Kestrel.

The Linux deployment uses this model with [[Nginx]] as a [[Reverse Proxy]]. The application must account for forwarded request information and operate as a managed service.

# References

[[aspnetcore3andangular9_3ed.pdf]]
