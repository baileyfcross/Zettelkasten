2026-09-06 19:44

Status: #baby

Tags: [[Direct Linear System Solvers]]

# Partial Pivoting

Partial pivoting selects the largest available absolute entry in the current column as the next pivot and interchanges rows to place it in the pivot position.

Used with [[Gaussian Elimination]], it avoids division by a zero pivot and usually limits numerical error. The row exchanges can be recorded by a [[Permutation Matrix]].

At elimination step $j$, the search is restricted to the unprocessed rows at or below the pivot. Moving the largest-magnitude candidate into row $j$ keeps the elimination multiplier no larger than one in magnitude, limiting one common source of [[Error Propagation]].

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[statisticalcomputingincplusplusandr.pdf]]
