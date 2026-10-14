2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Circuit-Centric Quantum Parameter Reduction

The original strongly entangling block permits a general three-parameter one-qubit unitary at each location and a controlled version of such a unitary at each connection. Much of this parameterization is redundant because a controlled unitary can be diagonalized into basis changes, a controlled phase, and local phase operations that merge with neighboring gates.

After commuting and merging those operations, a block can be represented with controlled phase gates, single-parameter $X$ rotations, and a reduced collection of one-qubit gates. Except for boundary effects in the final layer, the paper bounds the description at roughly $5n$ real parameters for $n$ qubits.

This reduction preserves the action of the [[Strongly Entangling Quantum Classifier Block]] up to global phase while making the model slimmer. It also illustrates why circuit identities and parameter tying matter when counting trainable capacity: the number of symbols in a naive gate diagram can overstate the number of independent model directions.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
