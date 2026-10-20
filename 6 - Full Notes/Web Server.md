2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# Web Server

A web server listens for network requests and passes them into a web application. It is distinct from the [[Web Host]], which provides the broader execution context and application services.

ASP.NET Core can use servers such as [[Kestrel]] and can also integrate with an external server such as [[Internet Information Services]] or operate behind an [[Nginx]] [[Reverse Proxy]].

Helidon SE instead embeds an immutably configured WebServer in the standalone application. Helidon 4 rebuilt that server as Helidon Níma on Java virtual threads, replacing the Netty-based reactive layer used by earlier releases while retaining explicit listener and routing configuration.

# References

[[aspnetcore3andangular9_3ed.pdf]]

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
