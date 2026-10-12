2026-09-14 21:00

Status: #baby

Tags: [[Transfer and Active Learning]]

# Active Learning Query Strategy

An active learning query strategy ranks unlabeled observations by the expected value of obtaining their labels from an oracle. The learner spends a limited labeling budget on selected cases rather than accepting a random labeled sample.

Strategies can target uncertainty, disagreement, expected performance improvement, representativeness, or combinations of these goals. Selection bias and variable labeling costs must be considered when assessing the resulting model.

Resampling can expose where a model is unstable: several models trained on slightly different subsets will disagree more in regions with little data. Those regions are candidates for new labels. In classification, cases near the current decision boundary—including a negative case that closely resembles positives—are informative because their labels can materially change the boundary.

# References

[[dataclassification.pdf]]

[[machinelearning_mit.epub]]
