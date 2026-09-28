2026-09-28 03:19

Status: #baby

Tags: [[Healthcare Fraud Analytics]]

# Supervised Provider Fraud Classification

Supervised provider fraud classification learns from provider profiles labeled through prior investigations or audits. Features can summarize billing volume, procedure mix, patient relationships, temporal behavior, and peer-relative deviations.

Confirmed fraud labels are rare, delayed, and shaped by earlier audit strategies, so the training set is not a neutral sample. Models should account for class imbalance and evaluate whether they generalize to new providers and schemes. A probability or ranking is most appropriate for prioritizing review, not declaring intent without investigation.

# References

[[healthcaredataanalytics.pdf]]
