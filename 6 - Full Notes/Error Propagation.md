2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Error Propagation

Error propagation describes how errors in input values and intermediate operations affect a computed result. Arithmetic may preserve, accumulate, cancel, or magnify those errors.

The algorithm and the underlying problem both matter. Stable procedures limit unnecessary growth, while an [[Ill-Conditioned Linear System]] can magnify even unavoidable small perturbations.

Repeated arithmetic carries earlier rounded values into later operations. Addition of very different magnitudes may lose the smaller contribution, while subtraction of nearly equal quantities can expose error through [[Catastrophic Cancellation]]; rearranging the computation can therefore change its final accuracy.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
