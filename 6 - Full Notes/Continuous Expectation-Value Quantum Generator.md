2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Continuous Expectation-Value Quantum Generator

A continuous quantum generator maps an externally sampled random vector $z$ and trainable parameters $\theta$ to a circuit state $|G_\theta(z)\rangle$. One Pauli-$Z$ expectation value is read from each qubit, producing a continuous feature vector with one component per data dimension after rescaling from $[-1,1]$ to $[0,1]$.

The benchmark injects each latent coordinate through $R_X$ rotations and repeats the injection after every variational-entangling block. This is the related but less pervasive reuploading pattern distinguished in [[Style-qGAN Latent Reuploading]]. It allows a $d$-dimensional sample to use only $d$ qubits.

The compact register hides a measurement cost. Each fixed $z$ must be executed many times to estimate all expectations before it yields one sample, so training and inference on hardware can be slow even though state-vector simulation evaluates the same output directly. [[Discrete Born-Sampling Quantum Generator]] makes the opposite qubit-shot tradeoff.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

