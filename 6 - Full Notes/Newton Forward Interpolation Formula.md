2026-10-03 16:11

Status: #baby

Tags: [[Interpolation Methods]]

# Newton Forward Interpolation Formula

Newton's forward formula interpolates equally spaced data near the beginning of a table. With $p=(x-x_0)/h$, it expands the value in leading forward differences:

$$f(x)=y_0+p\Delta y_0+\frac{p(p-1)}{2!}\Delta^2y_0+\cdots.$$

The formula is a [[Polynomial Interpolation|polynomial interpolant]] written in [[Factorial Polynomial|factorial form]]. It is efficient when a forward [[Difference Table]] is already available.

# References

[[numericalmethodsinengineeringandscience.pdf]]

