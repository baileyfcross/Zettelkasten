2026-09-30 00:59

Status: #baby

Tags: [[Linear Coding Theory]]

# Parity-Check Matrix

A parity-check matrix $P$ defines a linear code as the vectors $v$ satisfying $Pv=0$. For a received vector $r$, the product $Pr$ is its syndrome: zero indicates that the parity constraints hold.

If every column of $P$ is nonzero and distinct, a single-coordinate error produces the corresponding column as its syndrome. The error location can then be identified and corrected.

# References

[[linearalgebra.pdf]]
