2026-09-28 04:01

Status: #baby

Tags: [[Adaptive Image Delivery and Caching]]

# Device-Pixel-Ratio Client Hint

The device-pixel-ratio hint communicates the relationship between CSS pixels and device pixels. Multiplying a display slot by this ratio estimates the source resolution needed to avoid undersampling.

Always serving the maximum density can waste bytes where bandwidth, memory, or visual content does not justify it. A server may choose a lower effective density and report that choice so the client interprets intrinsic dimensions correctly. See [[Content-DPR Response Header]].

# References

[[highperformanceimages.pdf]]
