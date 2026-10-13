2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# SVG Symbol Sprite

An SVG symbol sprite stores reusable vector definitions in one document. Individual icons reference a named symbol, allowing shared delivery while preserving resolution-independent geometry.

Symbols can support shapes and styling more naturally than icon fonts, but external-reference behavior and feature support must be considered for target clients. Inline sprites avoid another request but share the cache lifetime of the page; external sprites can be cached independently. See [[Data URI Cache Tradeoff]].

The `symbol` element is not rendered directly; a `use` instance supplies its visible position and dimensions. A symbol's viewBox and `preserveAspectRatio` rules let each instance scale from the same internal geometry, while inherited fill and stroke values allow one definition to adopt context-specific colors. External sprites reduce repeated HTML but historically imposed same-origin, stylesheet, paint-server, and shadow-DOM compatibility constraints, so the chosen delivery form must be tested as well as cached.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
