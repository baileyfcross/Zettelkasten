2026-10-01 00:39

Status: #baby

Tags: [[Affine and Projective Transformations]]

# Window-to-Viewport Transformation

A window-to-viewport transformation maps a selected rectangle in object or world space into a rectangle in screen space. The window chooses which portion of the model is visible; the viewport chooses where and how large that portion appears on the display.

The mapping translates the window's lower-left corner to the origin, scales its width and height to those of the viewport, and translates the result to the viewport's screen position. Independent horizontal and vertical scale factors can distort the image when the aspect ratios differ, so proportional display requires preserving the window's ratio.

# References

[[mathematicsforcomputergraphicsandgameprogramming.pdf]]
