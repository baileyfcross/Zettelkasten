2026-10-31 21:16

Status: #baby

Tags: [[REST API Testing Deployment and Real-Time Features]]

# Server-Sent Events API

A Server-Sent Events API keeps an HTTP response open so the server can deliver a stream of text events to a client. It is one-directional: the server pushes updates, while client commands continue through other requests.

The book presents SSE as a serverless real-time option alongside WebSockets, event-driven messaging, and push notifications. An implementation must handle connection limits, reconnection, event identifiers, authorization, and intermediary timeouts even though the transport begins as HTTP.

# References

[[masteringrestapis.epub]]
