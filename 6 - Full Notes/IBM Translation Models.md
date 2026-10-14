2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# IBM Translation Models

The IBM translation models are a sequence of probabilistic [[Word Alignment]] models developed from bilingual corpora. Model 1 learns lexical correspondences from co-occurrence; Model 2 adds relative word position; Model 3 adds fertility and null-word behavior; Model 4 improves phrase movement; and Model 5 constrains invalid configurations.

Training begins with many possible links and repeatedly reallocates probability toward word pairs and sentence alignments that reinforce one another. This expectation-maximization process turns raw sentence pairs into a probabilistic bilingual lexicon. The models established the noisy-channel foundation of [[Statistical Machine Translation]], even though their one-directional word assumptions motivated later segment and symmetric alignment methods.

# References

[[machinetranslation.epub]]
