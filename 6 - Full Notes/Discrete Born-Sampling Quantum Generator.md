2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Discrete Born-Sampling Quantum Generator

A discrete quantum generator encodes a probability distribution directly in computational-basis probabilities, $P_i(\theta)=|\langle i|G_\theta\rangle|^2$. One measurement of the trained circuit therefore returns one sample from the learned grid without estimating expectation values or supplying an external latent-noise vector.

For $d$ data dimensions and $r$ precision qubits per dimension, the circuit uses $n=rd$ qubits and represents $2^r$ positions along each axis. This gives efficient one-shot sampling but makes precision consume qubits linearly in dimension, as detailed by [[Discrete Quantum Generator Grid Resolution]].

The architecture's entropy comes from quantum measurement. [[Uniform Jitter for Discrete Quantum Samples]] can spread each grid output into a continuous neighborhood when hardware offers too few precision qubits, but that postprocessing does not increase the information learned by the circuit.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

