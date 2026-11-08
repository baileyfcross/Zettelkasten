2026-09-06 20:41

Status: #baby

Tags: [[Progressive Web Application Capabilities]] [[ASP.NET Core API Security and Caching]] [[REST API Security and Access Control]]

# Cross-Origin Resource Sharing

Cross-Origin Resource Sharing is an HTTP policy mechanism through which a server permits selected browser origins, methods, or headers to access its resources. It controls browser enforcement when the client and API do not share the same origin.

An ASP.NET Core application registers and applies a CORS policy in its middleware configuration. Production settings should name the intended origin rather than granting every origin access without need.

The book frames CORS as a controlled exception to the browser's same-origin policy. Server response headers state permitted origins, methods, headers, and credential behavior, while a preflight request lets the browser check a non-simple cross-origin operation before sending the actual request.

The server, not client-side JavaScript, defines which cross-origin reads the browser may allow. An Access-Control-Allow-Origin wildcard and broad method list demonstrate the mechanism, but a production policy should narrow origins and operations to the consumers that require them because CORS is a browser access policy rather than API authentication.

# References

[[aspnetcore3andangular9_3ed.pdf]]
[[hands-onrestfulwebserviceswithaspnetcore3.pdf]]
[[masteringrestapis.epub]]

[[prorestfulapiswithmicronaut.epub]]
