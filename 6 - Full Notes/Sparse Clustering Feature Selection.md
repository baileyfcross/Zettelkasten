2026-09-14 21:34

Status: #baby

Tags: [[Unsupervised Feature Selection for Clustering]]

# Sparse Clustering Feature Selection

Sparse clustering attaches weights to features and penalizes those weights so that many become exactly zero. Clustering and feature selection are then solved together: dimensions that do not help the partition lose influence.

Sparsity improves interpretability and can protect distances from irrelevant dimensions. The penalty level controls the selected set, and an overly strong penalty can erase weak features whose value appears only through interaction with others.

# References

[[dataclustering.pdf]]

