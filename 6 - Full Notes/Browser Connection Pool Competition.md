2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Browser Connection Pool Competition

Under connection-limited protocols, many small image requests occupy the browser’s finite pool and queue behind one another or compete with more important resources. Opening additional connections also pays transport setup and congestion costs.

HTTP/2 multiplexing reduces the need for parallel connections, but all streams still share bandwidth and prioritization. Consolidation can remain useful for very small assets, though its benefit is smaller than under older per-request connection patterns. See [[HTTP2 Stream Priority for Images]].

# References

[[highperformanceimages.pdf]]
