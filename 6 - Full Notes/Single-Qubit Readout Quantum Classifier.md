2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Single-Qubit Readout Quantum Classifier

A single-qubit readout turns the final state of the circuit-centric model into a binary classification score. Measuring the first qubit in state $1$ sums the squared magnitudes of the second half of the computational-basis amplitude vector, producing a probability $p(q_0=1\mid x,\theta)$.

Classical postprocessing adds a learned bias $b$ and assigns class $1$ when $p+b>0.5$. Equivalently, the score can be recovered from the expectation value of a Pauli-$Z$ measurement on the first qubit. Repeated circuit executions estimate the probability rather than revealing it exactly in one run.

The absolute squares and summation act as a weightless nonlinear layer after the [[Quantum Circuit as a Symmetric Unitary Neural Layer|unitary transformation]]. Because the unitary action on amplitudes is linear, this readout is roughly quadratic in the transformed amplitudes; higher-order separation requires a feature construction such as [[Tensorial Quantum Feature Map]].

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
