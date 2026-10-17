2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Hardware Deployment

For hardware deployment, the authors train a separate three-qubit collider model with five latent dimensions but reduce the generator from two layers to one to limit circuit depth and noise. Each generated event component is estimated from 1,000 circuit shots, and the resulting circuit is translated to the native operations of the target device.

On IBM's five-qubit `ibmq_santiago` superconducting processor, $10^5$ generated events retain the broad marginal shapes and correlations but degrade to KL divergences of $0.677$, $0.223$, and $0.336$ for $s$, $t$, and $y$. These values are substantially worse than the noiseless two-layer benchmark, and the comparison also changes circuit depth, so it is evidence of feasibility rather than a controlled hardware-equivalence test.

Producing the IBM sample took about one week. During that interval the device could be recalibrated, making calibration drift part of the observed result and illustrating the sampling cost discussed in [[Finite-Shot Quantum Generator Calibration]].

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

