2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Amplitude Encoding for Circuit-Centric Classification

Amplitude encoding associates a classical feature vector with the computational-basis amplitudes of a quantum state. An $N$-component real input is normalized and embedded into a $2^n$-component state with $n=\lceil\log_2 N\rceil$ qubits, padding the vector when its length is not a power of two.

This encoding makes the classifier narrow in qubit count because a register of $n$ qubits stores $2^n$ amplitudes. It does not make arbitrary data loading efficient: preparing a general amplitude vector still requires resources linear in the feature dimension. Efficient or approximate preparation therefore depends on exploitable input structure.

Normalization can distort datasets whose relevant information includes vector length rather than only direction. [[Noninformative Padding for Quantum Amplitude Encoding]] offers one response, while [[Tensorial Quantum Feature Map]] uses multiple encoded copies to create higher-degree features at the cost of more qubits and preparation work.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
