2026-10-14 09:10

Status: #baby

Tags: [[Circuit-Centric Quantum Classification]]

# Noninformative Padding for Quantum Amplitude Encoding

Noninformative padding appends constant components to a classical input before amplitude normalization. The padding width can raise the total dimension to an exact power of two, allowing every computational-basis amplitude of the chosen qubit register to be used.

Zero padding solves only the dimension mismatch. Nonzero constant padding also creates ancillary feature-space dimensions and makes the normalized state nonhomogeneous in the original variables. This can preserve some information that ordinary normalization would discard and can supply constant terms to later polynomial feature constructions.

The constants are called noninformative because they do not vary from example to example, but they still alter the geometry of the encoded data. Their choice is therefore part of the preprocessing and feature-map design for [[Amplitude Encoding for Circuit-Centric Classification]], not a neutral storage operation.

# References

[[2018 - Circuit-centric quantum classifiers.pdf]]
