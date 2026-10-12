2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]]

# Clustering Wrapper Feature Selection

A wrapper method evaluates feature subsets by actually clustering the data and measuring the resulting solution. The search treats the clustering procedure and its quality criterion as the evaluator of a candidate representation.

Wrappers can capture interactions among features and the biases of the chosen algorithm, but repeated clustering makes them expensive. They can also overfit an internal quality measure, so stability and external domain interpretation remain necessary.

# References

[[dataclustering.pdf]]

