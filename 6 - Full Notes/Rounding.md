2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Rounding

Rounding replaces a number with the nearest representable value at the retained precision. The first discarded digit determines whether the final retained digit is increased.

Its error is generally no more than half a unit in the last retained place. Repeated operations can still accumulate or amplify these small [[Round-Off Error|round-off errors]].

Floating-point arithmetic rounds after each operation, not only when values are first read. Consequently, changing evaluation order can change the sequence of intermediate rounded values even when the exact algebraic result is unchanged.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
