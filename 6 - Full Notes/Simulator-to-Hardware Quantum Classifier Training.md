2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Simulator-to-Hardware Quantum Classifier Training

Simulator-to-hardware training first optimizes a noise-free circuit classically and then calibrates the resulting parameters around that solution on the physical device. The first stage minimizes the fidelity loss on 200 training examples to obtain $\Theta_{sim}$, avoiding noisy and expensive global exploration on hardware.

The second stage searches a neighborhood of $\Theta_{sim}$ for corrections $\delta\Theta$ and sets $\Theta_q=\Theta_{sim}+\delta\Theta$. Parameters are scanned in overlapping pairs while the others remain fixed, and the largest improvements occur in the earliest layers. In the circle and hypersphere cases, this local calibration reduces the device-simulator discrepancy from several percentage points to roughly one or two points.

The paper maximizes device accuracy on the dataset it calls $D_{test}$ during this second stage. Consequently, the resulting $A_q$ is best interpreted as a hardware-calibrated result rather than an accuracy measured on an untouched holdout set. The procedure primarily demonstrates mitigation of systematic device errors.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
