2026-10-14 18:20

Status: #baby

Tags: [[Quantum Optical Neurons]]

# Optical Neuron Classical-Model Equivalence

Discretizing the input and probe fields over $N$ spatial cells maps the optical classifier to

$$G_{b,w}(x)=\sigma\!\left(|w\cdot x|^2+b\right),$$

where the input field becomes a complex vector $x$, the trainable probe becomes weights $w$, and $b$ is a learned scalar bias. The interferometer physically evaluates the overlap whose squared magnitude supplies the first nonlinearity; a scalar sigmoid then produces the binary output.

The paper interprets this as a composition of a real-valued neuron with $N$ weights, square-absolute-value activation, and no bias, followed by a one-weight neuron with sigmoid activation and bias. This formal equivalence explains the phrase “quantum optical neuron,” but it also limits the claim: the demonstrated device corresponds to a unit-depth learning element, not an arbitrary multilayer network or a replacement for every [[Perceptron]] architecture.

# References

[[2024 - Quantum optical classifier with superexponential speedup.pdf]]
