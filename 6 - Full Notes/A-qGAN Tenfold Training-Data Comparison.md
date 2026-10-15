2026-10-15 10:16

Status: #baby

Tags: [[A-qGAN Anomaly Detection in High-Energy Physics]]

# A-qGAN Tenfold Training-Data Comparison

The headline sample-efficiency comparison trains each qGAN on 100 Standard Model events and its parameter-matched classical GAN on 1,000 events containing the same quantum subset. At seven compressed features, both methods achieve a Graviton ROC-AUC of about 0.96, while the qGAN's reported Higgs ROC-AUC is 0.92 versus 0.87 for the classical model. With only three features, the classical models perform better.

These results show comparable accuracy under the paper's deliberately unequal training-set budget; they do not show that the quantum model dominates when both methods receive identical data. The comparison also holds parameter counts approximately equal, which tests capacity per parameter but may constrain the classical baseline more strongly than an unconstrained production model.

Repeated trials have large standard deviations because both adversarial training and dataset reshuffling are volatile. Moreover, Standard Model collider events are plentiful, so reducing their count is not itself the main HEP bottleneck. The result is best understood as evidence worth testing on data-scarce tasks, larger feature spaces, equal-data baselines, and models beyond classical simulation.

# References

[[2023 - Quantum Generative Adversarial Networks For Anomaly Detection In High Energy Physics.pdf]]
