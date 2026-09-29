2026-09-28 04:01

Status: #baby

Tags: [[Image Request Consolidation]]

# Icon Font Consolidation

An icon font maps vector glyphs to interface symbols so many icons travel in one font resource and can inherit CSS color or size. It consolidates requests and uses scalable outlines.

The font approach also inherits font-loading behavior, glyph semantics, hinting, and accessibility problems. A missing font can hide every icon, multicolor artwork is awkward, and code points may be meaningless to assistive technology. Use it only when those tradeoffs fit better than [[SVG Symbol Sprite|SVG symbols]].

# References

[[highperformanceimages.pdf]]
