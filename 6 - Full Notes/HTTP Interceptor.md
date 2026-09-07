2026-09-06 20:41

Status: #baby

Tags: [[Web Identity and Access Control]]

# HTTP Interceptor

An Angular HTTP interceptor participates in outgoing requests and incoming responses handled by HttpClient. It can apply cross-cutting behavior such as attaching an authentication token or responding consistently to an authorization failure.

The interceptor centralizes behavior that would otherwise be repeated in every [[Data Service]]. Unlike a [[Service Worker]], it operates within the Angular request flow rather than as a browser background worker.

# References

[[aspnetcore3andangular9_3ed.pdf]]
