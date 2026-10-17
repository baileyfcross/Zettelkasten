2026-10-16 17:54

Status: #baby

Tags: [[Variational Quantum Wasserstein Anomaly Detection]]

# Quantum AnoGAN Convergence Comparison

Across the tested circuit and neural-network depths, quantum and classical Wasserstein AnoGAN models converge to a similar mean fraud-detection F1 score of about $0.84$. The classical generators generally reach that level in fewer iterations, although their dense layers also contain more parameters than the single-qubit-rotation layers used in the quantum circuits.

Depth has only a modest effect on the final score. Deeper classical networks converge slightly more slowly in the reported configuration, whereas deeper quantum circuits converge slightly faster. Individual runs of both model types sometimes fail to converge, consistent with the continuing instability of adversarial optimization even after adopting [[WGAN-GP Gradient Penalty Objective|WGAN-GP]].

Each plotted point averages at least 70 independent training runs, with bootstrapped 95 percent confidence intervals. That replication makes the parity result more informative than a single successful run, but the experiments use noiseless classical circuit simulation and do not include an end-to-end hardware runtime comparison.

# References

[[2021 - Anomaly detection with variational quantum generative adversarial networks.pdf]]
