2026-09-28 04:01

Status: #baby

Tags: [[SVG Authoring and Optimization]]

# SVG Text-to-Outline Tradeoff

Converting SVG text to outlines makes letter shapes independent of whether the client has the intended font. It can preserve a logo or other tightly controlled artwork.

The conversion replaces compact characters with path coordinates, often increasing file size and removing searchable, selectable, and accessible text semantics. Keeping text as text is preferable when font availability and layout can be managed; outlining is a deliberate fidelity tradeoff, not a universal optimization.

Live SVG text also permits anchoring, per-span styling, text paths, and DOM measurement, but its exact glyph widths depend on the font actually loaded. A fallback stack and tolerant alignment can preserve meaning when the preferred font is unavailable. When outlining is unavoidable, an explicit accessible label should restore the word or phrase that the paths no longer expose.

# References

[[highperformanceimages.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
