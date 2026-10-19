2026-10-18 22:56

Status: #baby

Tags: [[Enterprise Social Identity Security]]

# Jakarta Security Authentication Mechanisms

Jakarta Security gives an enterprise application a portable way to define how an HTTP request is authenticated. An authentication mechanism obtains evidence from the request, asks an identity store to validate it, and reports an authentication result to the container. Built-in basic and form mechanisms cover common cases, while custom mechanisms can integrate another credential or external identity flow.

This separation keeps protocol handling distinct from identity data. The mechanism knows how to converse with the caller; the [[Jakarta Security Identity Store]] knows how credentials map to a valid identity and groups. Social login built with [[Soteria OpenID Connect Authentication]] follows the same architectural goal even when the evidence arrives through an external provider rather than a local password form.

# References

[[enterprisesocialforthejavaplatform_sharesmashupslikesandwaystointe.epub]]
