2026-10-16 17:27

Status: #baby

Tags: [[Quantum Chebyshev Modeling]]

# Quantum Chebyshev Boundary-Condition Encoding

Quantum Chebyshev boundary-condition encoding uses an explicit continuous-variable feature map so a differential-equation model can be evaluated at selected interior and boundary coordinates. Boundary values can then enter the loss directly, while [[Quantum Chebyshev Model Differentiation]] supplies derivatives for the governing differential residual.

This is easier to formulate than a purely implicit amplitude-encoded model, where the function exists only as a global vector of basis amplitudes and individual coordinates are not exposed through the same pointwise interface. The [[Explicit and Implicit Quantum Model Duality]] preserves both capabilities: train and constrain the model explicitly, then use the [[Quantum Chebyshev Transform]] when amplitude encoding or sampling is needed. The paper presents this as an application route rather than a completed differential-equation benchmark.

# References

[[2023 - Quantum Chebyshev Transform Mapping Embedding Learning and Sampling Distributions.pdf]]
