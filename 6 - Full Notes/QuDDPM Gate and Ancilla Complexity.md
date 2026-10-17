2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Gate and Ancilla Complexity

Under a one-dimensional nearest-neighbor model, the paper estimates that scrambling an $n$-qubit ensemble toward an approximate random design requires a number of circuit layers linear in $n$. With $O(n)$ local gates per layer, the forward diffusion therefore uses $O(n^2)$ gates.

The complete backward process has similar asymptotic gate complexity and may add at most $n_A\leq 2n$ ancilla qubits for measurement-conditioned denoising. Its total gate estimate is also $O(n^2)$.

These are construction-level asymptotics rather than end-to-end hardware costs. They do not include the repeated SWAP tests needed to estimate ensemble losses, optimization iterations, device connectivity conversions, error correction, or the sample complexity of all pairwise fidelities.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

