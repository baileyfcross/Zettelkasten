2026-09-05 16:28

Status: #baby

Tags: [[Natural Language Understanding Systems]] · [[Deep Feature Representation]] [[Large Language Model Foundations]]

# Word Embedding

A word embedding represents a word as a dense numerical vector learned from patterns of use. Words that occur in similar contexts tend to receive nearby representations, providing a graded notion of semantic similarity.

Unlike one-hot identifiers, embeddings share statistical information among related words. They give language models and classifiers features that can generalize beyond phrases seen verbatim in a [[Training Dataset]].

Kelleher describes word2vec as learning vectors from neighboring-word co-occurrence: words used in similar textual contexts tend to acquire similar vectors. Those vectors can become numerical inputs to a [[Recurrent Neural Network]] for language processing. Proximity reflects patterns in a training corpus; it should not be mistaken for a complete account of a word's meaning in every context.

Deep feature engineering uses these learned vectors as distributed representations rather than sparse word identities. Recurrent, gated, and other sequence models can then operate on dense inputs whose geometry reflects corpus context.

In a transformer, token embeddings provide the learned content vectors to which [[Positional Encoding]] is added. Training moves tokens used in related contexts into useful geometric relationships, but the initial embedding is only a starting representation; attention layers make it context dependent.

Alpaydin uses word2vec to show that shared contexts can preserve relations as well as proximity. City names can cluster together, country adjectives can form another region, and similar city-to-country offsets permit vector analogies. This arithmetic reflects regularities of the training corpus; it is evidence of a learned representation, not a logical dictionary of meaning.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]

[[aiassistants.epub]]

[[deeplearning_mit.epub]]

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[machinelearning_mit.epub]]
