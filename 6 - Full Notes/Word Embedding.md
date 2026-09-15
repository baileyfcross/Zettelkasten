2026-09-05 16:28

Status: #baby

Tags: [[Natural Language Understanding Systems]]

# Word Embedding

A word embedding represents a word as a dense numerical vector learned from patterns of use. Words that occur in similar contexts tend to receive nearby representations, providing a graded notion of semantic similarity.

Unlike one-hot identifiers, embeddings share statistical information among related words. They give language models and classifiers features that can generalize beyond phrases seen verbatim in a [[Training Dataset]].

Kelleher describes word2vec as learning vectors from neighboring-word co-occurrence: words used in similar textual contexts tend to acquire similar vectors. Those vectors can become numerical inputs to a [[Recurrent Neural Network]] for language processing. Proximity reflects patterns in a training corpus; it should not be mistaken for a complete account of a word's meaning in every context.

# References

[[aiassistants.epub]]

[[deeplearning_mit.epub]]
