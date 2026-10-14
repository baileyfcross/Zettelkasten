2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Tensorial Quantum Feature Map

A tensorial quantum feature map prepares $d$ copies of an amplitude-encoded state, $|\psi(x)\rangle^{\otimes d}$. Tensor products turn the original components into degree-$d$ products; for example, two copies of $(x_1,x_2)$ contain $x_1^2$, two copies of $x_1x_2$, and $x_2^2$ as amplitudes.

These monomials lift the input into a larger feature space and can support more nonlinear decision boundaries. The paper compares the construction loosely with a polynomial kernel, while noting that the classifier's measurement introduces an additional quadratic nonlinearity, so the two degrees are not directly equivalent.

The expressiveness is paid for in width and preparation cost. With $n=\lceil\log_2 N\rceil$ qubits per encoded input, $d$ copies require $dn$ qubits before the extra training ancilla. The map is therefore most useful when the higher-degree separation justifies the additional resources identified by [[Circuit-Centric Quantum Classifier Resource Scaling]].

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
