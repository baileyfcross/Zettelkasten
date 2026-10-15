2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Hardware Demonstration

The hardware experiment runs a three-feature A-qGAN on the five-qubit superconducting processor `ibmq_belem`. It focuses only on Standard Model versus Graviton classification, trains on subsets of 50 background events for five epochs, and estimates each expectation value with $10^4$ shots.

Under those restrictions, the hardware ROC-AUC is 0.74, compared with 0.81 for noiseless qGAN simulation and 0.84 for the classical GAN. The reduction cannot be attributed to device noise alone because the hardware run also uses fewer events and far fewer training epochs than the noiseless numerical experiment.

The demonstration establishes executable feasibility: state preparation, adversarial parameter updates, local discriminator measurement, and anomaly scoring can all be completed on a real processor. It does not establish hardware advantage or large-scale readiness. A stronger test would isolate noise from training-budget changes, repeat calibrations across devices, report total circuit and shot cost, and extend beyond three compressed features. [[A-qGAN Noise Robustness Evidence]] describes the separate noisy-simulator comparison.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
