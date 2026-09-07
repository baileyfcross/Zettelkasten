2026-09-06 20:31

Status: #baby

Tags: [[HTTP API Integration]]

# Observable

An observable represents a sequence of values or events that a consumer can subscribe to over time. It fits asynchronous client behavior because the producer can emit a result, an error, or later updates without blocking the caller.

Angular [[Angular HttpClient|HttpClient]] returns observables for HTTP operations. Components and services can transform, retry, or react to those streams, and an activity log can observe form changes without repeatedly polling the form model.

# References

[[aspnetcore3andangular9_3ed.pdf]]
