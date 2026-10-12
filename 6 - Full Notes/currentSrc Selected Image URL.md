2026-09-28 04:01

Status: #baby

Tags: [[Responsive Image Selection]]

# currentSrc Selected Image URL

The `currentSrc` property reports the actual image candidate selected by the browser after evaluating `srcset`, `sizes`, and any enclosing `picture` sources. The original `src` attribute may be only a fallback and need not equal the fetched URL.

Inspecting `currentSrc` is useful for testing responsive behavior, analytics, and debugging incorrect candidates. Code should treat the value as the browser’s present choice, which may change if viewport or density conditions change.

# References

[[highperformanceimages.pdf]]
