2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Compression with Gzip or Brotli

SVG markup contains repeated element names, attributes, numbers, and syntax, making it highly compressible with general-purpose text compression. Serving SVG with Gzip or Brotli can therefore remove substantial transfer overhead without changing document semantics.

Transport compression complements structural cleanup rather than replacing it. Removing editor metadata, redundant groups, and excessive precision shrinks the source that the compressor sees and also reduces parsing or rendering complexity. See [[Automated SVG Optimization]].

# References

[[highperformanceimages.pdf]]
