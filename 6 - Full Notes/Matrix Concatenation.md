2026-09-18 17:13

Status: #baby

Tags: [[Game Linear Algebra]]

# Matrix Concatenation

Matrix concatenation multiplies transformation matrices so several spatial operations can be applied as one composite transform. The resulting matrix preserves the sequence of operations encoded by the multiplication order.

Scale, rotation, and translation therefore cannot be rearranged casually. A world transform that scales, then rotates, then translates describes different behavior from a matrix that performs those operations in another order.

# References

[[gameprogrammingincplusplus.pdf]]
[[gameprogrammingalgorithmsandtechniques.pdf]]
