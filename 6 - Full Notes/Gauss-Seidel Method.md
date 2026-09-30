2026-09-06 19:44

Status: #baby

Tags: [[Iterative Linear System Methods]]

# Gauss-Seidel Method

The Gauss-Seidel method updates the components of an approximate solution sequentially. Each new component is used immediately when computing the remaining components in the same iteration.

This often converges faster than the [[Jacobi Method]], though convergence is still not automatic. It is the special case $\omega=1$ of [[Successive Over-Relaxation]].

With the splitting $A=D+L+U$, the matrix form is $(D+L)x^{(k+1)}=b-Ux^{(k)}$. The triangular solve explains how each freshly computed component enters the remaining updates immediately.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
