2026-11-08 16:45

Status: #baby

Tags: [[Spring Web and Service Interfaces]]

# Spring RestClient

Spring `RestClient` is a fluent synchronous HTTP client for constructing a request, supplying headers or a body, exchanging it, and mapping the response. Its builder can carry a base URL and shared transport configuration, and Boot customizers can apply timeouts or other policy consistently.

The client is appropriate when the calling code uses an imperative model and does not need a reactive stream. It can also serve as the generated transport behind a [[Spring HTTP Service Interface]], separating the remote contract from the mechanics of each call. A synchronous API still needs connection pooling, deadlines, error mapping, and resilience suited to the dependency.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
