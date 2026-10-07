2026-10-07 17:18

Status: #baby

Tags: [[Nonlinear Optimization Methods]]

# Blind Random Search

Blind random search samples candidate points from the allowed parameter region and retains the point with the best objective value. It makes few structural assumptions and does not require gradients or a smooth objective.

The method can explore separated basins, but its chance of entering a small high-quality region falls rapidly as dimension grows. It is best understood as a baseline or exploratory global search whose result depends on the proposal distribution, number of samples, and reproducible random stream.

# References

[[statisticalcomputingincplusplusandr.pdf]]
