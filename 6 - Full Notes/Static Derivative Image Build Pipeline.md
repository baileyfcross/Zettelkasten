2026-09-28 04:01

Status: #baby

Tags: [[Image Derivative Workflows]]

# Static Derivative Image Build Pipeline

A static image pipeline generates required derivatives ahead of deployment. A task runner or build script can resize, crop, watermark, choose formats, compress, and optimize a bounded source catalog into versioned outputs.

Precomputation removes transformation latency from user requests and allows slower, more efficient encoders. Its cost is regeneration and storage: changing dimensions or quality may require rebuilding the whole catalog. See [[Image Build System Suitability]] and [[MozJPEG Optimization]].

# References

[[highperformanceimages.pdf]]
