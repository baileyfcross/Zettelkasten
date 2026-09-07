2026-09-06 19:44

Status: #baby

Tags: [[Numerical Eigenvalue Methods]]

# QR Algorithm

The QR algorithm repeatedly factors $A_k=Q_kR_k$ and reverses the factors to form $A_{k+1}=R_kQ_k$. The new matrix is similar to the old one because $A_{k+1}=Q_k^TA_kQ_k$.

Under appropriate conditions, the sequence approaches triangular form and reveals eigenvalues on the diagonal. Preliminary reduction makes the iterations cheaper.

# References

[[appliedlinearalgebraandoptimizationusingmatlab.pdf]]

