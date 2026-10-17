2026-10-16 22:51

Status: #baby

Tags: [[Quantum Generative Architecture Performance]]

# Architecture and Preprocessing Dominance in Quantum Generation

Across six of the eight tested datasets, changing the continuous, standard-discrete, or copula-discrete architecture and its normalization affects KL divergence more than switching between QCBM and QGAN training. QGAN is usually slightly better, but that advantage is smaller than the spread created by representation choices.

Discrete circuits outperform continuous circuits on every three-dimensional dataset and almost every two-dimensional dataset, with the copula/PIT combination providing the strongest results on structured X and O distributions. Mixed-Gaussian and stock returns show smaller preprocessing differences because their dependencies are closer to the structure already handled by the baseline models.

The result shifts design attention from the optimizer label to the interface between data and circuit. [[Probability Integral Transform for Quantum Generation]] is most effective when paired with [[Quantum Copula Generator Architecture]], while a generic circuit gains less from the same transformation.

# References

[[2023 - A performance characterization of quantum generative models.pdf]]

