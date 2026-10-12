2026-09-06 20:31

Status: #baby

Tags: [[ASP.NET Core Application Architecture]] [[ASP.NET Core Page and MVC Development]]

# MVC Controller

An MVC controller is a server-side class whose action methods handle routed requests. A controller does not have to render an HTML view: in a Web API it can return structured data such as JSON for a browser client.

Controllers sit behind the [[HTTP Request Pipeline]] and are reached through [[Endpoint Routing]]. This lets an Angular [[Single-Page Application]] request data without moving server-side presentation logic into the client.

In the WWTravelClub design, controllers translate requests into application-layer operations and select view models or results; domain and persistence responsibilities stay outside the presentation boundary.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[aspnetcore3andangular9_3ed.pdf]]
[[c80andnetcore30moderncross-platformdevelopment.pdf]]
