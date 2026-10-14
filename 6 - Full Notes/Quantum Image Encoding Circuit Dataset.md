2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Quantum Image Encoding Circuit Dataset

A quantum image encoding circuit dataset stores a separately optimized state-preparation circuit for every classical image. The Fashion-MNIST study resizes each $28\times28$ image to $32\times32$, flattens the pixels in a snake pattern, and represents it on 11 qubits as a [[Flexible Representation of Quantum Images|FRQI state]].

All 60,000 training images and 10,000 test images are encoded at three sparse-ansatz depths, with corresponding QASM circuits released for reuse. This avoids repeating the expensive classical circuit optimization in later experiments, but storage and preprocessing still scale with the number of examples. The artifact is therefore a benchmarking resource rather than a general on-demand loading oracle.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
