2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon Server Request Path Parameter

A Helidon route can declare a named path segment such as `/{name}` and retrieve the matched value from the server request's path parameters. This lets one handler serve a family of resource paths without parsing the raw URL manually.

In the greeting service, the handler obtains `name` and combines it with the current greeting before sending a JSON response. The parameter belongs to the route match established by [[Helidon HTTP Routing]], not to a global request variable.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
