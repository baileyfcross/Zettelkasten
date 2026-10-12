2026-09-15 18:17

Status: #baby

Tags: [[Rotoscopy and Motion Tracking]]

# Spline Handle Choice for Rotoscopy

Spline type affects how a roto contour bends between control points. A Bezier spline can hold a sharp change of direction through its handles, while a B-spline tends to produce a smoother curve with tension distributed across neighboring points. A smooth contour with unnecessarily many points becomes difficult to animate and may wobble. The best choice follows the subject's actual silhouette rather than a habit of adding vertices. See [[Segmenting Moving Roto Shapes]] for why separate shapes also reduce contour complexity.

# References

[[digitalvisualeffectsandcompositing.pdf]]
