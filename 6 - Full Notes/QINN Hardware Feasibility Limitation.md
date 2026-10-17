2026-10-16 23:00

Status: #baby

Tags: [[Quantum Invertible Generative Models]]

# QINN Hardware Feasibility Limitation

The QINN study is a proof-of-principle simulation rather than a hardware demonstration. The authors state that available noisy intermediate-scale devices cannot support even the model required for their basic generative task.

Practical execution would have to estimate output expectations, parameter-shift derivatives for a full Jacobian, and the quantities used by the inverse-state-preparation loss. Those repeated measurements would be exposed to finite-shot error, gate noise, and the depth of both the forward and inverse-preparation circuits.

The reported parameter efficiency therefore measures representational capacity within the simulated training setup. It does not establish faster training, cheaper sampling, noise robustness, or quantum advantage on a real device.

# References

[[2023 - Generative Invertible Quantum Neural Networks.pdf]]

