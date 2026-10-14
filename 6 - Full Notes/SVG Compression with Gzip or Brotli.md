2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Compression with Gzip or Brotli

SVG markup contains repeated element names, attributes, numbers, and syntax, making it highly compressible with general-purpose text compression. Serving SVG with Gzip or Brotli can therefore remove substantial transfer overhead without changing document semantics.

Transport compression complements structural cleanup rather than replacing it. Removing editor metadata, redundant groups, and excessive precision shrinks the source that the compressor sees and also reduces parsing or rendering complexity. See [[Automated SVG Optimization]].

Precompressing assets can save server work, but the response must identify the actual content encoding in its HTTP headers. Compression and packaging are therefore delivery concerns as well as file-generation steps: a small `.svgz`-like payload is unusable if an intermediary or browser is not told how to decode it.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
