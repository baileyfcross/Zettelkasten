2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# Kestrel

Kestrel is the cross-platform web server used by ASP.NET Core applications. A [[Web Host]] can configure it as the server that receives HTTP traffic and feeds requests into the application's middleware pipeline.

In Linux deployment, Kestrel commonly runs the application behind an [[Nginx]] [[Reverse Proxy]] rather than serving public traffic directly. On Windows, ASP.NET Core can instead use an IIS in-process hosting arrangement.

# References

[[aspnetcore3andangular9_3ed.pdf]]
