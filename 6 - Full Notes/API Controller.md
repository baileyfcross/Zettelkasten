2026-09-06 20:52

Status: #baby

Tags: [[HTTP API Integration]] [[REST Framework and Serverless Implementations]]

# API Controller

An API controller is an ASP.NET Core class whose actions expose application behavior over HTTP. Routing selects the controller and action, model binding constructs inputs, and the returned action result becomes the HTTP response.

The controller should coordinate the transport boundary rather than own persistence details. It validates the request, calls an injected repository or service, and translates the outcome into an appropriate response.

In the book's ASP.NET Core implementation, an API controller derives from `ControllerBase`, uses `[ApiController]` and route attributes, and maps HTTP methods to actions. Model binding and validation prepare inputs, while action results select the response body and status without coupling the public contract to the database representation.

# References

[[aspnetcore3andreact.pdf]]
[[masteringrestapis.epub]]
