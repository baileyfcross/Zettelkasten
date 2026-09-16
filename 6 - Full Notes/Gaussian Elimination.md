2026-09-06 19:44

Status: #baby

Tags: [[Direct Linear System Solvers]] · [[FEM Mathematical Foundations]]

# Gaussian Elimination

Gaussian elimination uses [[Elementary Row Operation|row operations]] to transform an [[Augmented Matrix]] into upper triangular or [[Row Echelon Form]]. The resulting system is completed by [[Back Substitution]].

A small or zero pivot can amplify error or halt the naive algorithm. [[Partial Pivoting]] and [[Scaled Partial Pivoting]] rearrange rows to improve reliability.

After assembly and boundary-condition enforcement, a finite element model becomes a simultaneous linear system. Gaussian elimination provides a direct route to its nodal unknowns by triangularization followed by back substitution.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[finiteelementanalysis_aprimer.pdf]]
