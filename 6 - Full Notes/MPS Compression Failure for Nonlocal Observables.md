2026-10-17 11:34

Status: #baby

Tags: [[Scalable Error-Mitigated Quantum Simulation]]

# MPS Compression Failure for Nonlocal Observables

Matrix-product-state compression retains the largest Schmidt coefficients, but a discarded sector can still control a selected nonlocal observable. In the kicked-Heisenberg benchmark, half of the Schmidt coefficients are tied to one component of a deliberately skewed entangled pair. Compressing the bond dimension to half of its exact value removes that entire component.

For the 122-qubit, 30-step verifiable instance, the exact global parity is about $0.997$, while the half-dimension MPS gives about $0.016$. A large retained norm or enormous bond dimension therefore does not guarantee an accurate observable when the measurement targets discarded structure. This is the paper's mechanism for the sharp transition from accurate to nearly useless generic classical simulation; it does not rule out a customized classical algorithm for the same instance.

# References

[[2024 - Scalability of quantum error mitigation techniques from utility to advantage.pdf]]

