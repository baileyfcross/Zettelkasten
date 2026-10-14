2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Quantum Classifier Margin Robustness

For an argmax quantum classifier, the prediction margin is the gap between the correct class score and the largest competing score. Finite-shot fluctuations or hardware noise change the label only if their effect is large enough to close that gap, so two correctly simulated examples can have very different experimental reliability.

The Fashion-MNIST hardware results are not monotonic in circuit depth partly because encoding quality, classifier quality, noise, and per-example margins interact. A high noiseless accuracy does not determine hardware accuracy unless the score gaps are also known. Margin distributions therefore provide a more informative robustness diagnostic than accuracy alone when evaluating [[Single-Optimization Multiclass Quantum Classifier|multiclass quantum classifiers]].

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
