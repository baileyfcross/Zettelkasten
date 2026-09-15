2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# K-Prototypes Dissimilarity Balance

K-prototypes dissimilarity combines squared numeric deviation from means with categorical mismatch from modes. A weighting parameter balances the scale of the categorical portion against continuous variation.

If the balance is too small, category agreement has little effect; if too large, numeric geometry disappears. The implementation should expose the weight as validated configuration rather than bury it in the update routine.

# References

[[dataclusteringincplusplus.pdf]]

