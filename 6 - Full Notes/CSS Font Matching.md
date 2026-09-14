2026-09-14 01:58

Status: #baby

Tags: [[CSS Web Typography]]

# CSS Font Matching

CSS font matching compares a request against available faces in a declared family list. The source describes matching family, stretch, style, weight, size, and required characters, trying alternate families when a face or glyph cannot satisfy the request.

Generic families provide the final fallback. [[CSS Font Face Rule|`@font-face`]] descriptors tell the matcher which requests a downloaded resource can satisfy, while [[CSS Font Synthesis]] controls whether missing bold or italic faces may be simulated.

# References

[[css_thedefinitiveguide.pdf]]
