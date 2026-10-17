2026-10-17 14:21

Status: #baby

Tags: [[Natural-Gradient Optimization of Optical Quantum Circuits]]

# Coordinate Dependence of Euclidean Gradient Descent

A coordinate gradient is steepest only under the Euclidean metric implicit in those coordinates. In polar coordinates, for example, the physical line element is

$$ds^2=dr^2+r^2d\phi^2,$$

so an angular increment represents a distance proportional to the radius rather than the same distance everywhere.

The corresponding metric is $\operatorname{diag}(1,r^2)$, and the natural-gradient angular component is scaled by $1/r^2$. Treating $(r,\phi)$ as ordinary Cartesian coordinates would therefore give a direction that depends on the chosen representation rather than solely on the underlying point.

At $r=0$, the angular coordinate is redundant and the metric becomes singular. This elementary example anticipates the same issue in parameterized quantum circuits: multiple parameter settings can describe the same physical state.

# References

[[2021 - Natural Gradient Optimization for Optical Quantum Circuits.pdf]]

