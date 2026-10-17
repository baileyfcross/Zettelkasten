2026-10-16 22:03

Status: #baby

Tags: [[Style-qGAN Monte Carlo Event Generation]]

# Style-qGAN Cross-Platform Portability Test

The same one-layer, three-qubit style-qGAN is executed on IBM superconducting hardware and IonQ trapped-ion hardware after compilation through platform-specific translation layers. The IBM device requires choosing a connected three-qubit subset, whereas IonQ's all-to-all connectivity avoids the same routing constraint.

Because external IonQ access limits the experiment to $10^3$ generated events per platform, the two-dimensional histograms are sparse. Both platforms nevertheless reproduce the principal $s$-$t$, $t$-$y$, and $y$-$s$ structures, suggesting that the high-level generator can be ported between distinct native gate sets.

The experiment is explicitly not a hardware-technology comparison. It lacks matched calibration, execution volume, error mitigation, and uncertainty analysis, so it shows qualitative portability rather than equivalence or superiority of either platform.

# References

[[2022 - Style-based quantum generative adversarial networks for Monte Carlo events.pdf]]

