2026-09-14 01:58

Status: #baby

Tags: [[CSS Filters Blending Clipping and Masking]]

# CSS Clipping Paths

A CSS clipping path defines a hard boundary outside which an element is not painted. The path can reference an SVG clip path or use a basic shape such as an inset rectangle, circle, ellipse, or polygon.

Clipping changes visible paint but not box layout, so surrounding content still responds to the original box. This differs from [[CSS Shape Outside]], which changes float wrapping, and [[CSS Masks]], which can create partial transparency.

In SVG terms, a clipping path behaves like a one-bit visibility test: each point is either inside or outside vector geometry. That makes a clip cheaper and sharper than a graduated mask, and the clipped region can also restrict pointer hit testing. A clip may apply to a single shape or to a composited group without altering the source geometry underneath.

# References

[[css_thedefinitiveguide.pdf]]
[[usingsvgwithcss3andhtml5.pdf]]
