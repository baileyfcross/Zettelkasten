2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Simulator-Hardware Architecture Reversal

On a state-vector simulator, the continuous generator is cheap because exact Pauli expectations are computed in one evaluation and the circuit uses only one qubit per feature. The wider discrete circuit is slower to simulate because its state dimension grows with $rd$ and the experiment explicitly samples measurement outcomes.

On quantum hardware, the comparison reverses. A discrete output needs one measurement, while every continuous sample needs enough repeated shots to estimate an expectation vector with acceptable variance. The simulator therefore removes the continuous model's largest hardware cost while amplifying the discrete model's width cost.

Simulation time cannot consequently stand in for deployment time. Resource comparisons must translate each architecture into device executions, shots, circuit depth, qubit count, and noise exposure, as in [[Quantum Generative Runtime Scaling]].

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

