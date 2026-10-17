2026-10-17 17:30

Status: #baby

Tags: [[Quantum Algorithm Execution and Verification]]

# Grover Diffusion Operator

For the equal superposition

$$
|s\rangle=\frac{1}{\sqrt N}\sum_{x=0}^{N-1}|x\rangle,
$$

the Grover diffusion operator is $U_s=2|s\rangle\langle s|-I$. In the computational basis it reflects every amplitude about their mean.

After the oracle negates the marked amplitude, this reflection raises it while slightly lowering the unmarked amplitudes. Repeating the oracle and diffusion reflections rotates the state toward the marked basis vector rather than testing candidates independently.

# References

[[Introduction to Quantum Computing-NASA.pdf]]

