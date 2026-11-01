2026-10-31 21:16

Status: #baby

Tags: [[REST Framework and Serverless Implementations]]

# Serverless API Gateway

A serverless API gateway receives an HTTP request, applies edge policies, and invokes the configured cloud function or backend integration. It can provide routing, authentication, validation, throttling, caching, stages, metrics, and response transformation without a permanently managed application server.

The book's AWS case combines API Gateway with Lambda, while its Azure case combines API Management with Functions. Managed infrastructure reduces provisioning work but leaves the public contract, function errors, provider limits, and backend idempotency under application ownership.

# References

[[masteringrestapis.epub]]
