2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Industrial Quantum Generative Resource Estimates

The largest simulated benchmark uses twelve qubits and about 174 gates, placing its noiseless circuit shape near current NISQ device sizes but not demonstrating execution under device noise. Scaling the same encodings to industrial dimensions rapidly exceeds those resources.

For a 100-dimensional finance or virtual-patient example, the paper estimates about 100 qubits and 400 gates for the continuous architecture. A copula-discrete design with sixteen precision qubits per variable would require about 1,600 qubits and more than 52,000 gates.

Image-like data around $10^5$ dimensions would require on the order of $10^5$ qubits and $10^6$ gates even for the continuous design, with roughly another order of magnitude for a discrete architecture. These are structural extrapolations that omit error correction and routing, so they show the scale gap rather than a deployment plan.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

