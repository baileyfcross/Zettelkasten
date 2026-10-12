2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Round-Off Error

Round-off error is the difference introduced when an exact number or arithmetic result is replaced by a finite-precision representation.

Subtraction of nearly equal numbers can expose it through cancellation, and multiplication or division can propagate it. A large [[Matrix Condition Number]] can amplify small data or rounding errors into a large solution error.

Round-off arises at storage and after arithmetic whenever the exact result is not a representable floating-point number. Its effect depends on both the sequence of operations and their scale, which is why algebraically equivalent formulas can have very different [[Numerical Stability]].

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
