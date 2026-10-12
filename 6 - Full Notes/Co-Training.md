2026-09-14 21:00

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# Co-Training

Co-training uses two sufficiently informative views of each observation. A classifier trained on one view assigns confident pseudo-labels that enlarge the labeled set available to the classifier using the other view, and the exchange repeats.

The method relies on complementary views whose errors are not identical. If both views share the same bias or confident predictions are wrong, reciprocal pseudo-labeling can reinforce mistakes rather than add independent evidence.

# References

[[dataclassification.pdf]]
