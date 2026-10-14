2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Classical Linear-Combination Quantum Gradient

A classical linear-combination quantum gradient represents the derivative of a parameterized gate as a short weighted sum of ordinary unitary gates. Each term is evaluated by a modified circuit, and a classical processor combines the measured results instead of coherently implementing the entire linear combination.

For the paper's one-qubit parameterization, one angular derivative is another gate with a $\pi/2$ shift, while the other derivatives require two shifted gates. A controlled-gate derivative becomes half the difference between controlled positive and negative derivative gates. Without parameter sharing, a model derivative consequently uses two or four unitary terms depending on the gate type.

An ancilla-based interference routine estimates the required real overlaps between the original and modified circuit states. The original and derivative circuits differ at only one gate, so only that location needs the extra conditional control. This gives the [[Circuit-Centric Quantum Classifier]] an analytical-gradient training route, although every overlap is still a statistical estimate requiring repeated measurements.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
