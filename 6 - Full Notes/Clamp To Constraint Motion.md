2026-09-28 20:13

Status: #baby

Tags: [[Blender Keyframe Animation and Rigging]] [[Blender Constraint Systems]]

# Clamp To Constraint Motion

A Clamp To constraint restricts an object's translated position to a target curve while allowing another source, such as direct transforms, a driver, or physical forces, to provide the movement. Unlike Follow Path, it does not inherently turn the object to face along the curve.

The method requires a suitable cardinal-axis alignment. It is useful when the curve should act as a spatial rail rather than as the complete timing and orientation controller.

Blender maps the owner's actual location property along the selected main axis to a position on the curve. A cyclic option moves the owner between path ends when the mapped location passes a boundary, while Influence blends the clamped result with the unconstrained transform. This reinforces the distinction between location-to-curve mapping and time-driven path animation.

# References

[[howtocheatinblender27x.pdf]]
[[modelingandanimationusingblender.pdf]]
