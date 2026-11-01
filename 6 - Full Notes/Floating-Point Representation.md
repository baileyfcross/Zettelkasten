2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]] [[SIMD Numerical Accuracy and Statistics]]

# Floating-Point Representation

Floating-point representation stores a real number using a sign, a finite-precision mantissa, a base, and an integer exponent. It covers a wide range of magnitudes but only a finite set of values.

Numbers that cannot be represented exactly must be rounded or chopped. The resulting [[Round-Off Error]] influences numerical algorithms, especially repeated arithmetic and ill-conditioned problems.

In a normalized binary representation, the sign, significand, and exponent occupy fixed-width fields. That format gives wide dynamic range but nonuniform spacing: adjacent representable numbers are farther apart at larger magnitudes, and values outside the exponent range overflow or underflow.

For a Java `float`, a finite significand means that adding a small value to a sufficiently large value may round back to the large operand. SIMD does not change that representation; it changes grouping and evaluation order, so a vector reduction can be correct yet differ slightly from a scalar left-to-right sum.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
