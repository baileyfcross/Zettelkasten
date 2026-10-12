2026-09-28 04:01

Status: #baby

Tags: [[Image Derivative Workflows]]

# Master Image Fetch Latency

An on-demand transformer cannot begin decoding until the master image is available. Distance to origin, connection setup, bandwidth, and master size therefore sit directly on the first-request latency path.

Keeping masters near the transformation service and caching them can reduce the delay. A processing master may also be capped near the largest deliverable size so the service does not repeatedly transfer and decode studio-scale files when no derivative can use that detail. See [[In-Memory Image Expansion]].

# References

[[highperformanceimages.pdf]]
