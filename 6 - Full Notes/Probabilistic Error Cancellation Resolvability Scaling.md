2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Probabilistic Error Cancellation Resolvability Scaling

Probabilistic error cancellation represents an ideal circuit as a signed quasiprobability combination of implementable noisy circuits. For one globally depolarizing channel, the optimal construction can improve relative resolvability, but the maximum gain is modest and rapidly approaches one as the number of qubits grows.

Local depolarizing noise produces a less favorable scaling. The quasiprobability variance costs multiply across noisy gates, so correcting $n$ qubits through $L$ noisy layers introduces a factor that decays exponentially in $nL$. Even if cancellation perfectly restores the ideal mean, its improvement eventually loses to the accumulated sampling overhead.

For a single local-noise instance, the outcome can be better or worse depending on how strongly that channel concentrates the cost. The useful regime is therefore controlled by both inverse-noise overhead and recovered landscape separation, not cancellation accuracy alone.

In a dense $N\times L$ circuit with realistic sparse Pauli-Lindblad noise and error density $\epsilon$, the quasiprobability normalization grows as $\gamma\approx e^{\epsilon NL}$. PEC's best-case sampling overhead is $\gamma^2\approx e^{2\epsilon NL}$ because every shot is rescaled by a signed factor of magnitude $\gamma$. This observable-agnostic Schrödinger-picture correction is quadratically more expensive in the leading noise factor than observable-aware ZNE or TEM for the same modeled circuit.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]
