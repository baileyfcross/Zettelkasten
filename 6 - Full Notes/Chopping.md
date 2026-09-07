2026-09-06 19:44

Status: #baby

Tags: [[Numerical Error and Conditioning]]

# Chopping

Chopping discards all digits beyond the retained precision without adjusting the final retained digit.

It is simpler than [[Rounding]] but introduces a one-sided error whose magnitude can approach a full unit in the last retained place. Repeated chopping can create systematic numerical bias.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

