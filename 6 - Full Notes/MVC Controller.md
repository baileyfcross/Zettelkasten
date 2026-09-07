2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]]

# MVC Controller

An MVC controller is a server-side class whose action methods handle routed requests. A controller does not have to render an HTML view: in a Web API it can return structured data such as JSON for a browser client.

Controllers sit behind the [[HTTP Request Pipeline]] and are reached through [[Endpoint Routing]]. This lets an Angular [[Single-Page Application]] request data without moving server-side presentation logic into the client.

# References

[[aspnetcore3andangular9_3ed.pdf]]
