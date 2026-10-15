2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Composite Anomaly Score

The A-qGAN score combines information from both adversarial components after training. A residual component uses the squared fidelity $|\langle x|G\rangle|^2$ between an embedded test event and the generator state. A discriminator component combines the final-qubit $Z$ expectations obtained when the discriminator processes the event and the generator output.

A mixing coefficient $\alpha\in[0,1]$ controls how much the score relies on the discriminator rather than on the fidelity term. Using both signals is intended to make detection less sensitive to instability in either the generator or discriminator alone. The paper labels events by comparing the resulting score with a calibrated threshold.

The two components have different scaling risks. The discriminator uses a local one-qubit readout, while the global fidelity may become exponentially concentrated as the register grows. The composite form therefore does not by itself guarantee scalable separation. [[A-qGAN Fidelity Concentration Limitation]] isolates that issue, and [[A-qGAN Alpha and Threshold Selection]] describes how the paper tunes the mixture empirically.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
