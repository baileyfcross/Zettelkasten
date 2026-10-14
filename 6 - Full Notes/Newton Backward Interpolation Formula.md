2026-10-03 16:11

Status: #baby

Tags: [[Interpolation Methods]]

# Newton Backward Interpolation Formula

Newton's backward formula interpolates equally spaced data near the end of a table. With $p=(x-x_n)/h$, it uses differences anchored at the final entry:

$$f(x)=y_n+p\nabla y_n+\frac{p(p+1)}{2!}\nabla^2y_n+\cdots.$$

It represents the same interpolating polynomial as other exact formulas but arranges the computation around $x_n$, where the backward differences and powers of $p$ are most convenient.

# References

[[numericalmethodsinengineeringandscience.pdf]]

