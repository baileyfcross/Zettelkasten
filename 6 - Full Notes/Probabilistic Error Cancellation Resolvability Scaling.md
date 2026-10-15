2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Probabilistic Error Cancellation Resolvability Scaling

Probabilistic error cancellation represents an ideal circuit as a signed quasiprobability combination of implementable noisy circuits. For one globally depolarizing channel, the optimal construction can improve relative resolvability, but the maximum gain is modest and rapidly approaches one as the number of qubits grows.

Local depolarizing noise produces a less favorable scaling. The quasiprobability variance costs multiply across noisy gates, so correcting $n$ qubits through $L$ noisy layers introduces a factor that decays exponentially in $nL$. Even if cancellation perfectly restores the ideal mean, its improvement eventually loses to the accumulated sampling overhead.

For a single local-noise instance, the outcome can be better or worse depending on how strongly that channel concentrates the cost. The useful regime is therefore controlled by both inverse-noise overhead and recovered landscape separation, not cancellation accuracy alone.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
