2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG Pointer Event Hit Testing

SVG hit testing converts a mouse or touch location into the topmost eligible graphical element. The `pointer-events` property can make the fill region, stroke region, both, or neither sensitive, with variants that also consider whether those regions are painted or visible. Its default, `visiblePainted`, reacts only to visible painted fill and stroke regions.

Opacity does not remove a region from hit testing, so a fully transparent fill can enlarge or regularize a target without changing its appearance. `pointer-events: none` instead lets the event pass through a decorative foreground layer to content underneath. Clipping can restrict the interactive region, while `display: none` makes an element ineligible regardless of the property.

The fill and stroke hit regions follow actual vector geometry: fill rules define interior areas, and dash patterns, caps, joins, and width define the [[SVG Stroke Geometry|stroke region]]. [[SVG Line Markers|markers]] remain decorations of their host path rather than independent targets. Once a target is found, [[SVG Pointer Coordinate Conversion]] is needed only when the handler must locate the pointer in user coordinates.

# References

[[usingsvgwithcss3andhtml5.pdf]]

