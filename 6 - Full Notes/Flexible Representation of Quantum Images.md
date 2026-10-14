2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Flexible Representation of Quantum Images

The Flexible Representation of Quantum Images (FRQI) represents a $2^n\times2^n$ grayscale image with $2n$ position qubits and one color qubit. An equal superposition addresses every pixel position $j$, while the color qubit rotates by an angle proportional to the normalized intensity $x_j$:

$$
|\psi\rangle=\frac{1}{2^n}\sum_j|j\rangle\left[\cos\!\left(\frac{\pi x_j}{2}\right)|0\rangle+\sin\!\left(\frac{\pi x_j}{2}\right)|1\rangle\right].
$$

FRQI needs only one more qubit than direct amplitude encoding and preserves absolute pixel intensities without normalizing the pixel vector itself. Typical FRQI image states can have relatively low entanglement, which enables [[Variational FRQI State Preparation]], but exact preparation still has CNOT count quadratic in the number of pixels.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
