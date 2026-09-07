2026-09-06 20:31

Status: #baby

Tags: [[HTTP API Integration]]

# ASP.NET Core Health Checks

ASP.NET Core Health Checks is middleware and service support for running registered [[Health Check|health checks]] and exposing their aggregate status through an endpoint. A check can test application state or an external dependency and return a structured result.

Because health-check middleware participates in the ordinary [[HTTP Request Pipeline]], it can answer a diagnostic route without requiring an [[MVC Controller]]. A response writer can convert its results into JSON for an Angular client.

# References

[[aspnetcore3andangular9_3ed.pdf]]
