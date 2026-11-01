2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]] [[SIMD Numerical Accuracy and Statistics]]

# Mantissa

The mantissa is the finite string of significant digits stored in a [[Floating-Point Representation]]. Together with the base and exponent, it determines the represented value.

A longer mantissa provides finer relative precision. Because it has limited length, arithmetic results may need to be rounded or chopped before they can be stored again.

The book demonstrates the effect by adding small signed values around a `float` magnitude of $2^{25}$. At that scale, some low-order contributions fall below the representable spacing. Sequential and pairwise addition then expose different surviving bits because they create different intermediate magnitudes.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
