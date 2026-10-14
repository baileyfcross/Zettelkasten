2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Strongly Entangling Quantum Classifier Block

A strongly entangling classifier block applies a parameterized one-qubit gate to every active qubit and then a cyclic layer of controlled gates. A range parameter $r$ determines the separation between each control and target, and a classifier can stack blocks with different ranges to mix correlations at different distances.

For an $n$-qubit block, the controlled layer contains $n/\gcd(n,r)$ gates. When $r$ and $n$ are relatively prime, the cycle reaches every qubit, so the block can entangle or disentangle the full register rather than leaving independent residue classes.

The paper chooses this architecture as a data-agnostic way to give a shallow circuit access to both short- and long-range correlations. It remains a restricted subset of all $2^n$-dimensional unitaries, trading universal flexibility at exponential depth for polynomial circuit size. [[Circuit-Centric Quantum Parameter Reduction]] further removes redundant parameters from each block.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
