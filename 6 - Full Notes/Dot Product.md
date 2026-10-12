2026-09-16 23:45

Status: #baby

Tags: [[Cartesian Analytic Geometry]] · [[Vector Algebra and Geometry]] · [[R Matrix Systems and Scientific Models]]

# Dot Product

For planar vectors $u=(u_1,u_2)$ and $v=(v_1,v_2)$, the dot product is $u\cdot v=u_1v_1+u_2v_2$. The result is a scalar. It also satisfies $u\cdot v=\|u\|\|v\|\cos\theta$, so a zero dot product identifies perpendicular nonzero vectors and the sign records whether their angle is acute or obtuse.

With normalized vectors, a game can use the dot product directly as the cosine of the angle between directions. The sign quickly distinguishes whether a target is generally in front of, beside, or behind an object's facing direction.

In component form the dot product is the sum of paired component products in an orthonormal basis. Its geometric form makes it useful for extracting a component along a direction and for testing orthogonality without constructing the angle explicitly.

The student companion first implements the arithmetic in R as the sum of element-wise vector products and then uses the same row-by-column calculation to motivate [[Matrix Multiplication]]. This connects a simple vector expression to coupled scientific projections.

# References

[[gameprogrammingincplusplus.pdf]]
[[foundationsofmath.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]

[[mathematicalphysics.pdf]]

[[multivariableandvectorcalculus.pdf]]

[[rstudentcompanion.pdf]]
