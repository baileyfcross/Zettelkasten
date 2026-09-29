2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# Service Worker Image Interception

A service worker can intercept an image request and answer from a cache, fetch the network, or synthesize a response. This puts application-controlled logic between browser discovery and the returned bytes.

The interception does not remove decoding or compatibility requirements: the response must still be a valid representation for the requesting client. Service-worker strategies can improve repeat visits and offline behavior, but complex handlers can also add startup or routing latency to otherwise native requests.

# References

[[highperformanceimages.pdf]]
