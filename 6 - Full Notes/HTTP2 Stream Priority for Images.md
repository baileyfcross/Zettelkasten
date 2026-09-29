2026-09-28 04:01

Status: #baby

Tags: [[Browser Image Loading]]

# HTTP2 Stream Priority for Images

HTTP/2 can multiplex many responses on one connection and express relative stream priorities. This permits a browser or server to allocate bandwidth among images and critical resources without opening one connection per request.

Multiplexing removes some connection-pool pressure but not bandwidth contention. Treating every image equally can still delay styles, scripts, or an important hero image. Progressive formats offer an additional opportunity to prioritize the bytes that produce an early preview. See [[Sequential and Progressive JPEG]].

# References

[[highperformanceimages.pdf]]
