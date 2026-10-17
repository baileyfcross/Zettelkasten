2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Quantum Generator Ansatz Ablation

The quantum AnoGAN study compares four generator circuits. Three combine trainable single-qubit rotations with CNOT patterns, while a fourth contains no entangling gates. Rotation axes are either drawn from $X$, $Y$, and $Z$ once per run or fixed as a full $X$-$Y$-$Z$ sequence, and circuit depth repeats the trainable layer.

The full-rotation circuit performs best at depth one, while most randomly initialized circuits become statistically similar by depth three. Even the unentangled circuit is competitive beyond one layer. Because a simple classical upscaling layer also performs well, this result indicates that the fraud dataset is too easy to establish a benefit from quantum entanglement or greater circuit expressivity.

The ablation also exposes a measurement-specific effect: randomly selected $Z$ rotations can be invisible to a final $Z$ measurement, so extra layers increase the chance that useful noncommuting rotations appear. The authors use the simpler first circuit for later experiments because its performance is comparable while its classical simulation is cheaper.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
