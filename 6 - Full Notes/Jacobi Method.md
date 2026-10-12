2026-09-06 19:44

Status: #baby

Tags: [[Iterative Linear System Methods]]

# Jacobi Method

The Jacobi method rearranges each equation of a [[Linear System]] to solve for one unknown, then computes every component of the next approximation using only values from the previous iteration.

Because its updates are simultaneous, it is simple but may converge slowly or diverge. [[Strict Diagonal Dominance]] is a useful sufficient condition for convergence.

Writing $A=D+L+U$ with diagonal part $D$ gives the iteration $x^{(k+1)}=D^{-1}(b-(L+U)x^{(k)})$. Convergence from every initial guess occurs when the iteration matrix has spectral radius below one.

# References

[[numericalmethodsinengineeringandscience.pdf]]

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

[[linearalgebra.pdf]]
