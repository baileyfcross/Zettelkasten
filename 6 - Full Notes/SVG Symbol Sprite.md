2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# SVG Symbol Sprite

An SVG symbol sprite stores reusable vector definitions in one document. Individual icons reference a named symbol, allowing shared delivery while preserving resolution-independent geometry.

Symbols can support shapes and styling more naturally than icon fonts, but external-reference behavior and feature support must be considered for target clients. Inline sprites avoid another request but share the cache lifetime of the page; external sprites can be cached independently. See [[Data URI Cache Tradeoff]].

# References

[[highperformanceimages.pdf]]
