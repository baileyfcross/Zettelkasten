2026-10-15 10:25

Status: #baby

Tags: [[Error-Mitigation Trainability of Variational Quantum Algorithms]]

# Noise-Induced Cost Concentration

Local Pauli noise interleaved with a parameterized quantum circuit contracts the output state toward a state-independent fixed point. For an observable-based cost, this makes the noisy value approach the maximally mixed expectation, $\mathrm{Tr}(O)/2^n$, while the remaining parameter dependence is bounded by a polynomial prefactor times a factor that decays exponentially with circuit depth.

When the depth grows linearly or faster with the number of qubits, this contraction becomes exponential in system size. Cost values produced by different parameter settings then cluster together even if the corresponding ideal values remain separated. The landscape is not merely shifted: its usable vertical scale disappears beneath finite-shot fluctuations.

This mechanism is distinct from the random-circuit mechanism in [[Barren Plateau Gradient Scaling]], although both can produce exponentially weak optimization signals. The stated bound assumes local unital Pauli noise; it does not automatically extend to every coherent, correlated, or nonunital hardware error.

# References

[[2021 - Can Error Mitigation Improve Trainability of Noisy Variational Quantum Algorithms.pdf]]
