2026-09-16 00:09

Status: #baby

Tags: [[Ensemble and Semi-Supervised Classification]]

# Out-of-Bag Error

Out-of-bag error evaluates each training observation using only random-forest trees whose bootstrap samples omitted that observation. Aggregating these predictions provides an internal estimate of generalization without creating a separate validation set for that purpose.

It remains an estimate tied to the training population and does not replace a final independent test.

# References

[[essentialsofdatascience.pdf]]

