2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]] · [[Vector Algebra and Geometry]]

# Vector Norm

A vector norm measures vector magnitude. Common forms include the $1$-norm $\sum_i|x_i|$, Euclidean norm $(\sum_i x_i^2)^{1/2}$, and infinity norm $\max_i|x_i|$.

Norms provide distances between approximations, residual sizes, and stopping criteria for iterative methods. Different norms emphasize total, geometric, or worst-component error.

Game geometry most often uses the Euclidean norm for displacement and distance. When only a comparison is needed, [[Squared Vector Length]] avoids the square root while preserving which vector is longer.

For a Euclidean vector, the identity $\|v\|=\sqrt{v\cdot v}$ connects magnitude directly to the [[Dot Product]]. It also supplies the distance between two points by taking the norm of the difference of their [[Position Vector|position vectors]].

# References

[[gameprogrammingincplusplus.pdf]]
[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]

[[multivariableandvectorcalculus.pdf]]
