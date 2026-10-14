2026-10-03 16:11

Status: #baby

Tags: [[Numerical PDE Methods]]

# Dufort-Frankel Method

The Du Fort-Frankel method modifies the centered Richardson heat-equation scheme by replacing the central spatial value with an average involving the future and previous time levels. The resulting recurrence is explicit once two earlier levels are known.

This change removes the instability of the unmodified [[Richardson Scheme]] for the model heat equation. A separate one-step method is still needed to generate the first time level before the three-level recurrence can proceed.

# References

[[numericalmethodsinengineeringandscience.pdf]]

