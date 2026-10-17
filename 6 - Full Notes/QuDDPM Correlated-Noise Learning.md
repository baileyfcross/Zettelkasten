2026-10-16 23:13

Status: #baby

Tags: [[Quantum State Diffusion Models]]

# QuDDPM Correlated-Noise Learning

QuDDPM can learn a distribution of coherently misprepared quantum states rather than only an ideal target state. The paper simulates a two-qubit superposition exposed to either a correlated $XX$ rotation or a correlated $ZZ$ rotation, with the error type chosen probabilistically and its angle sampled from a range.

Only the $XX$ error populates the $|10\rangle$ component, so the generated ensemble's average fidelity with $|10\rangle$ provides an estimator of the $XX$ error probability after accounting for the known amplitude and angle distribution.

With 500 training and test states, the target statistic is $0.129$, while generated training and test values are $0.128$ and $0.133$. This is a simulated two-qubit characterization example, not a demonstration on measured device noise.

# References

[[2023 - Generative quantum machine learning via denoising diffusion probabilistic models.pdf]]

