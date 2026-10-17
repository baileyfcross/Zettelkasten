2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# Error Density in Layered Quantum Circuits

For sparse Pauli-Lindblad noise, the total noise accumulation factor can be written as $\gamma=(1+\epsilon)^{NL}\approx e^{\epsilon NL}$ for a dense circuit of $N$ qubits and $L$ layers. The parameter $\epsilon=\gamma^{1/(NL)}-1$ is the average error density per qubit per layer, while $\epsilon NL$ is the expected number of circuit errors relevant to a high-weight observable.

A typical noisy signal is attenuated by approximately $\gamma^{-1/2}\approx e^{-\epsilon NL/2}$. Small per-layer error is therefore not sufficient for scalability: when the circuit volume is large, the observable can fall below practical shot noise. This aggregate quantity controls the leading sampling costs compared in [[Observable-Aware and Observable-Agnostic Error Mitigation]].

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

