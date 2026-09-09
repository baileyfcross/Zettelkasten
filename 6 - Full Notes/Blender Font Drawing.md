2026-09-08 09:04

Status: #baby

Tags: [[Blender Viewport Drawing API]]

# Blender Font Drawing

Font drawing turns application data into readable viewport annotations. A reusable helper accepts two-dimensional coordinates, text, size, and a font identifier, then configures and draws the string through Blender's font API.

World-space data must first be projected into the viewport's two-dimensional region. After conversion, labels can follow an object's origin or a measurement midpoint as the view changes. Checking that projection returned a visible point prevents the drawing function from failing when the target lies outside the current view.

# References

[[blenderpythonapi.pdf]]
