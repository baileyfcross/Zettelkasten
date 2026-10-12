2026-09-14 21:00

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# Stacked Generalization

Stacked generalization trains a second-level model to combine predictions from several base classifiers. The combiner can learn that different models are reliable in different regions rather than using a fixed vote.

Its training inputs must be out-of-sample base predictions, commonly produced by cross-validation. Using predictions from models fitted on the same cases would leak training fit into the combiner and yield overoptimistic weights.

# References

[[dataclassification.pdf]]
