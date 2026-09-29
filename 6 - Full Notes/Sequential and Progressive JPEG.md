2026-09-28 04:01

Status: #baby

Tags: [[JPEG Encoding and Optimization]]

# Sequential and Progressive JPEG

A sequential JPEG encodes enough data to reconstruct each region at final quality as the scan advances, so the visible image commonly appears from top to bottom. A progressive JPEG distributes information across multiple scans.

Progressive delivery can show a coarse version of the whole image early and refine it as later scans arrive. This changes perceived completeness and can also improve compression, but scan structure and decoder behavior determine the actual benefit. See [[Progressive JPEG Scan Design]].

# References

[[highperformanceimages.pdf]]
