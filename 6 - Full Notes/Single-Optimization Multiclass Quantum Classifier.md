2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Single-Optimization Multiclass Quantum Classifier

A single-optimization multiclass quantum classifier distinguishes all $k$ classes with one parameterized circuit and one joint loss rather than training separate one-versus-one or one-versus-rest models. For an encoded state $|\widetilde\psi\rangle$, it predicts the index of the largest class observable:

$$
f(x)=\operatorname*{arg\,max}_i\langle\widetilde\psi|W^\dagger(\theta)O_iW(\theta)|\widetilde\psi\rangle.
$$

The Fashion-MNIST implementation trains circuit parameters and the [[Trainable Bitstring Observable Readout|class readout]] together under a log-softmax loss. One optimization loop does not automatically mean lower total quantum cost, because the number of shots needed to reliably choose among $k$ close scores grows with the number of classes and their margins.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
