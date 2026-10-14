2026-10-14 17:55

Status: #baby

Tags: [[Variational Quantum Image Classification]]

# Raw-Count Spread Decoherence Diagnostic

Raw-count spread measures how far each example's measured bitstring-frequency vector lies from the mean frequency vector across a test collection. The Fashion-MNIST study uses the average Euclidean distance as a high-dimensional analogue of standard deviation.

Depolarizing-like noise pulls distinct quantum states toward a common mixed state, causing their raw measurement distributions to cluster and the spread to shrink. Simulations show no consistent depth trend, but hardware spread falls as total CNOT count grows, supporting accumulated decoherence as the cause of degrading classifier accuracy. Because the metric ignores labels and learned post-processing, it diagnoses state collapse without being a disguised accuracy score.

# References

[[2024 - Classification of the Fashion-MNIST Dataset on a Quantum Computer.pdf]]
