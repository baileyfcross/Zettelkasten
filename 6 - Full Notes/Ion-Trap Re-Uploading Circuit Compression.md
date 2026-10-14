2026-10-14 09:18

Status: #baby

Tags: [[Single-Qubit Data Re-Uploading Classifiers]]

# Ion-Trap Re-Uploading Circuit Compression

The ion-trap implementation reduces active operations by treating $R_z$ as a phase-frame change rather than a laser-driven rotation. Changing the laser phase implements the $Z$ rotation without additional qubit-light interaction, leaving the data-dependent $Y$ rotation as the principal active gate in each layer.

It then combines an $R_z$ from one layer with the following layer's $R_y$ into a single rotation $R(\gamma,\delta)$ about an equatorial axis. Recursive phase updates preserve the intended sequence, so the compiled experiment uses roughly half as many active rotations as the theoretical alternating-gate circuit.

This is a pairwise hardware-aware rewrite, not a classical collapse of the whole model. The complete product of repeated data-dependent rotations produces the nonlinear behavior used by the [[Single-Qubit Data Re-Uploading Classifier]], while only adjacent gates are merged before execution.

# References

[[2021 - Single-qubit universal classifier implemented on an ion-trap quantum device.pdf]]
