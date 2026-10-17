2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Grover Phase Oracle

Grover search assumes an oracle $U_\omega$ that marks the desired basis state by changing its sign:

$$
U_\omega|x\rangle=
\begin{cases}
-|x\rangle,&x=\omega,\\
|x\rangle,&x\ne\omega.
\end{cases}
$$

The sign change does not alter the marked state's measurement probability immediately. It creates a relative phase that the [[Grover Diffusion Operator]] converts into increased amplitude. Oracle construction therefore contains the problem-specific work hidden by the simple search description.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

