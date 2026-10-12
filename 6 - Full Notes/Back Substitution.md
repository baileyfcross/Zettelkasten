2026-09-06 19:44

Status: #baby

Tags: [[Direct Linear System Solvers]]

# Back Substitution

Back substitution solves an [[Upper Triangular Matrix|upper triangular]] system from the final equation upward. The last equation determines the last unknown, whose value is inserted into each preceding equation.

It completes [[Gaussian Elimination]] and is also used after [[LU Decomposition]] or [[QR Decomposition]] has reduced a problem to an upper triangular system.

Each step subtracts contributions from already solved higher-index variables and divides by the current diagonal coefficient. A zero diagonal makes the triangular system singular, while a very small diagonal can amplify finite-precision error.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
