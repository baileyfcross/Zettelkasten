2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Selection Connections and Evaluation]]

# ReliefF Feature Selection

ReliefF ranks a feature by comparing value differences between nearby samples. Differences among nearest neighbors from the same class count against the feature, while differences between a sample and nearby members of other classes count in its favor.

The method extends Relief to multiclass data by weighting misses from each alternative class. Under balanced-neighborhood assumptions, its score can be expressed as alignment with a signed [[Sample Similarity Matrix]], making ReliefF a supervised special case of univariate spectral feature selection.

# References

[[spectralfeatureselectionfordatamining.pdf]]

