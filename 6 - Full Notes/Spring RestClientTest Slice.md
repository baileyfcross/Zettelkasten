2026-11-08 16:45

Status: #baby

Tags: [[Spring Application Testing]]

# Spring RestClientTest Slice

`@RestClientTest` loads the infrastructure for a selected outbound HTTP client and provides a mock server for its requests. The test can verify the URI, method, headers, and body the client produces and can supply a controlled response for mapping and error-handling assertions.

This isolates a [[Spring HTTP Service Interface]] or [[Spring RestClient]] adapter from the availability of the real provider. It proves the caller's contract but not the provider's implementation, network policy, or production authentication. Those concerns require contract verification and a bounded integration test.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
