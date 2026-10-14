2026-10-12 23:34

Status: #baby

Tags: [[Accessible Interactive and Animated SVG]]

# SVG Graphical Hyperlinks

The SVG `a` element can wrap text, shapes, images, reused icons, or groups to make their painted regions hyperlinks. Unlike an HTML image map, linked vector regions scale with the graphic and can receive CSS `hover`, `focus`, and active-state feedback. Transparent shapes can also be placed over a raster image to define responsive hotspots.

SVG links have no dependable default visual styling, so authors must provide a visible link treatment and an unmistakable focus state. A graphical link also needs an accessible name through text, `aria-label`, or [[SVG Accessible Names and Descriptions|SVG metadata]]. The book uses `xlink:href` for SVG 1 compatibility and notes the transition to the unprefixed `href` form in SVG 2.

A link is the one SVG interactive element with broadly established native keyboard behavior in the source's browser context. Scripts can adapt it into another control only if they also implement the expected keyboard actions and expose the matching ARIA role; where possible, native HTML controls remain safer. See [[SVG Keyboard Focus Management]].

# References

[[usingsvgwithcss3andhtml5.pdf]]

