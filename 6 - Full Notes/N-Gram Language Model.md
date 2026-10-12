2026-09-05 16:28

Status: #baby

Tags: [[Speech and Acoustic Modeling]] [[Large Language Model Foundations]]

# N-Gram Language Model

An n-gram language model estimates the probability of a word from a fixed number of preceding words. Counts in a text corpus provide probabilities for recurring sequences such as unigrams, bigrams, or trigrams.

Its limited history makes computation manageable during [[Speech Recognition Search]], but it cannot directly preserve distant context. Smoothing is needed when a plausible sequence was rare or absent in the training text.

The model can generate or score a sequence by chaining probabilities conditioned on the previous n minus one tokens. This makes next-token prediction explicit but also causes sparse counts and a fixed context limit, helping explain why neural representations and longer learned context replaced n-grams in modern language models.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[aiassistants.epub]]
