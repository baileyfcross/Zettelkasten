2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Client Hints Image Negotiation

Client hints move some responsive-image context from HTML into HTTP request headers. After the server opts in, a client can describe properties such as viewport width, device pixel ratio, requested resource width, network capacity, or a preference to save data.

The server uses those inputs to choose or generate a suitable representation and must identify the request dimensions that affect the response. This separates presentation markup from delivery logic, but increases caching and privacy complexity. See [[Accept-CH Opt-In]] and [[Vary Header for Image Variants]].

# References

[[highperformanceimages.pdf]]
