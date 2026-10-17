2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Quantum Generative Runtime Scaling

For fixed precision and block count, the estimated per-sample circuit depth grows linearly with data dimension for continuous, standard-discrete, and copula-discrete generators. The multiplicative constants differ because a continuous sample needs $N_s$ repeated shots, while each discrete measurement is already one sample.

With $N_b$ blocks, the continuous estimate is $N_sN_b(d+4)$. Standard-discrete sampling scales as $N_b(rd+2)$, while the copula circuit adds a one-time initialization depth $r(d-1)+1$ to a block depth that depends on $r$ but not directly on $d$.

For the study's assumption of more than 100 shots per expectation estimate, discrete sampling remains faster over practical precision choices. Continuous and discrete rates become comparable only beyond roughly 266 precision qubits per dimension for the fixed example, far above the roughly 32 bits associated with single-precision classical values.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

