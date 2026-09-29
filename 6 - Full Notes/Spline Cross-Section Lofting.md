2026-09-28 20:13

Status: #baby

Tags: [[Blender Efficient Modeling and Retopology]]

# Spline Cross-Section Lofting

Lofting constructs a surface through an ordered series of cross-sectional loops. In the Blender 2.7x workflow described by the book, curves define the profiles, are converted to mesh loops, and the LoopTools Loft operation connects corresponding points between them.

Consistent point counts and ordering help prevent twisted connections. A Solidify modifier can then give the lofted surface thickness while preserving the cross-sections as the primary description of form.

# References

[[howtocheatinblender27x.pdf]]
