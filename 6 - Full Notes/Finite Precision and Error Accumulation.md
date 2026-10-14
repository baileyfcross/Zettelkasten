2026-09-13 20:16

Status: #baby

Tags: [[Computational Methods and Formalization]]

# Finite Precision and Error Accumulation

Digital machines represent numbers with a finite number of bits, so many values must be rounded. In a long numerical calculation, small representation and round-off errors can accumulate until the result is no longer trustworthy.

Numerical methods control this risk through stable formulations, bounded errors, and checks on intermediate results. More hardware speed does not repair an unstable method; it can merely produce the wrong answer faster.

The same mathematical expression can admit several computational analogs with different error behavior. Centering data before forming sums of squares and scaling columns whose magnitudes differ greatly are examples of changing the representation of a problem before finite-precision operations amplify its disparities.

# References

[[computationalthinking.epub]]

[[statisticalcomputingincplusplusandr.pdf]]
