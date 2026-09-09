2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]] [[ASP.NET Core Page and MVC Development]]

# ASP.NET Core Middleware

ASP.NET Core middleware is a component registered in the [[HTTP Request Pipeline]] to inspect, handle, or pass along requests and responses. Middleware can supply narrowly selected features such as static files, HTTPS redirection, routing, health checks, or SPA fallback behavior.

Registration order is significant. A request is offered to middleware in pipeline order, so an earlier component can handle it before later endpoints or the Angular fallback are considered.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
