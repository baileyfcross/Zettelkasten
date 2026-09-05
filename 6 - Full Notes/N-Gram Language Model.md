2026-09-05 16:28

Status: #baby

Tags: [[Speech and Acoustic Modeling]]

# N-Gram Language Model

An n-gram language model estimates the probability of a word from a fixed number of preceding words. Counts in a text corpus provide probabilities for recurring sequences such as unigrams, bigrams, or trigrams.

Its limited history makes computation manageable during [[Speech Recognition Search]], but it cannot directly preserve distant context. Smoothing is needed when a plausible sequence was rare or absent in the training text.

# References

[[aiassistants.epub]]
