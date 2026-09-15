2026-09-15 09:23

Status: #baby

Tags: [[Data Science Deployment and Renewal]]

# Unseen Data Test Plan

A test plan estimates whether a model will generalize beyond the examples used to fit it. The book's golden rule is never to test a model on the same records used for training. A memorized training set, including its noise, can score well without predicting new cases reliably.

A training set fits candidates, a validation set supports comparing them, and a reserved test set estimates the final selected model's unseen-data performance. The test set must not guide algorithm selection or train the final model; otherwise it is no longer an independent check.

# References

[[datascience_mit.epub]]
