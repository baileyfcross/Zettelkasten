2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Quantum Circuit as a Symmetric Unitary Neural Layer

A quantum gate acting on amplitudes can be drawn as a linear neural-network layer with highly tied weights. A one-qubit gate connects repeated pairs of amplitude components with the same matrix entries, while a controlled version replaces part of that repeated pattern with identity connections and thereby breaks some of the symmetry.

Composing gates produces a sequence of square unitary layers. These layers preserve vector norm and never change their width, unlike an ordinary feedforward architecture whose weight matrices and hidden dimensions can be chosen independently. The gate entries also depend nonlinearly on a smaller set of rotation angles even though each layer is linear in the amplitude vector.

This graphical view explains both the compactness and the restriction of the [[Circuit-Centric Quantum Classifier]]. Many amplitude-to-amplitude connections are determined by parameter sharing and unitarity rather than learned separately. The measurement and threshold stages, not the unitary layers themselves, supply the model's explicit nonlinearity.

The symmetry can also be chosen to reproduce a familiar classical layer exactly. A [[Quantum Pyramidal Circuit]] made from number-preserving two-qubit rotations keeps unary inputs inside an $n$-dimensional invariant subspace. Restricted to that subspace, the larger $2^n\times2^n$ unitary acts as an $n\times n$ [[Orthogonal Matrix|orthogonal matrix]], giving the quantum gate pattern a precise matrix-vector interpretation rather than only a visual analogy.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]

[[2022 - Quantum Methods for Neural Networks and Application to Medical Image Classification.pdf]]
