2026-10-19 22:48

Status: #baby

Tags: [[Helidon WebServer and WebClient]]

# Helidon WebClient Redirect Chain

The Helidon WebClient redirect chain follows an HTTP response to the correct endpoint when redirect support is enabled. Client configuration can decide whether redirects are followed and set a maximum number so an unbounded redirect sequence does not continue indefinitely.

The example requests a redirect path, verifies that the final response is successful, and then reads the redirected entity. Redirect behavior is therefore part of the configured client request process rather than custom recursion in the application.

# References

[[helidonrevealed_apracticalguidetooraclesmicroservicesframework.epub]]
