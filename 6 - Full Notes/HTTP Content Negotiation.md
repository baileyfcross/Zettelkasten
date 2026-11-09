2026-10-31 21:16

Status: #baby

Tags: [[REST Resource Contracts and Data Handling]]

# HTTP Content Negotiation

HTTP content negotiation lets a client state which representation media types it can accept and lets the server select a supported response format. The same resource may consequently be represented as JSON, XML, or another agreed form without receiving a different conceptual identity.

The book uses the `Accept` header both for ordinary format selection and for media-type versioning. A server should describe the selected type in its response and return a clear failure when it cannot produce any representation acceptable to the client.

When none of the server's available representations satisfies the request's Accept values, the source uses HTTP 406 Not Acceptable to report the mismatch. This makes unsupported format selection a visible protocol outcome rather than silently returning a body the client did not declare it could process.

The Spring MVC example adds an XML message-converter dependency beside the default JSON converter. The DispatcherServlet's response pipeline then inspects the Accept header and selects a converter, and tests assert both the default JSON response and an explicitly requested XML response. Supporting a second format therefore requires converter configuration and regression tests, not a second conceptual resource.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]

[[masteringrestapis.epub]]

[[prorestfulapiswithmicronaut.epub]]
