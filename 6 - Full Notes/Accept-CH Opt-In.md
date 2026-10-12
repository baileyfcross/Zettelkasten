2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Accept-CH Opt-In

In the client-hints exchange described by the book, the server advertises which hints it is prepared to use through an `Accept-CH` response header. Subsequent requests in that browsing context can then carry the requested fields.

Opt-in avoids sending device and network characteristics indiscriminately to every origin. It also means the first response may arrive before hints are available, so the system needs a reasonable baseline representation and should not make correctness depend on adaptation. See [[Client Hints Image Negotiation]].

# References

[[highperformanceimages.pdf]]
