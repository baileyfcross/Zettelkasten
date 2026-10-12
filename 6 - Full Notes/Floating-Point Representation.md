2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Floating-Point Representation

Floating-point representation stores a real number using a sign, a finite-precision mantissa, a base, and an integer exponent. It covers a wide range of magnitudes but only a finite set of values.

Numbers that cannot be represented exactly must be rounded or chopped. The resulting [[Round-Off Error]] influences numerical algorithms, especially repeated arithmetic and ill-conditioned problems.

In a normalized binary representation, the sign, significand, and exponent occupy fixed-width fields. That format gives wide dynamic range but nonuniform spacing: adjacent representable numbers are farther apart at larger magnitudes, and values outside the exponent range overflow or underflow.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
