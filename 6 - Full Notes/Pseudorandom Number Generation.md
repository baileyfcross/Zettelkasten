2026-10-04 22:56

Status: #baby

Tags: [[R Probability Simulation and Curve Fitting]]

# Pseudorandom Number Generation

Pseudorandom number generation uses a deterministic algorithm to produce a sequence that behaves like draws from a specified distribution. Recording the generator state or seed makes a simulation repeatable even though the values are used as random outcomes.

Different distribution functions transform the generator into uniform, normal, binomial, and other draws. Reusing a seed can aid debugging, but repeated scientific runs should not accidentally reuse identical streams when independence is intended.

# References

[[rstudentcompanion.pdf]]
