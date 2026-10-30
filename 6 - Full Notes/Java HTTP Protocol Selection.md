2026-10-30 16:54

Status: #baby

Tags: [[Java Platform API Evolution]]

# Java HTTP Protocol Selection

Java HTTP protocol selection states the preferred HTTP version on a request or client while allowing compatibility fallback. In the book's Java 26 outlook, HTTP/3 can be requested explicitly and automatically falls back to HTTP/2 when the destination does not support it.

This permits gradual adoption without maintaining a separate client model. Protocol choice remains distinct from request construction and response handling, so the same `HttpRequest`, client, and body-handler abstractions continue to describe the exchange.

# References

[[java25andbeyond_modernjavamadeeasy.epub]]
