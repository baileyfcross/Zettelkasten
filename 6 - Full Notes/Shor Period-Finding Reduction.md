2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Shor Period-Finding Reduction

Shor factoring reduces the hard quantum portion to finding the period $r$ of

$$
f(x)=a^x\bmod N
$$

for a randomly chosen $a<N$ coprime to the composite integer $N$. The periodicity of modular powers supplies information that classical greatest-common-divisor calculations can convert into factors.

If $r$ is even and $a^{r/2}\not\equiv-1\pmod N$, then $\gcd(a^{r/2}\pm1,N)$ yields nontrivial factors. Failed random choices are retried, making the overall algorithm probabilistic even though the period-finding subroutine has structured quantum behavior.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

