2026-09-06 19:44

Status: #baby

Tags: [[Iterative Linear System Methods]]

# Iterative Refinement

Iterative refinement improves an approximate solution $x^{(k)}$ by computing the residual $r=b-Ax^{(k)}$, solving $Ay=r$ for a correction, and setting $x^{(k+1)}=x^{(k)}+y$.

The same coefficient matrix is reused. A few correction steps can recover accuracy lost while solving an [[Ill-Conditioned Linear System]], provided the residual is computed accurately enough.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

