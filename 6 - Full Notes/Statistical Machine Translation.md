2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# Statistical Machine Translation

Statistical machine translation learns translation choices from a large [[Parallel Corpus]] instead of requiring a human to enumerate every rule. A translation model estimates how likely a source expression is to correspond to a target expression, while a [[Statistical Language Model]] estimates whether the target sequence is plausible.

During decoding, the system searches for the target sentence that best combines both scores. This lets a less common word translation win when it creates a more coherent sentence. The approach handles frequent local patterns and ambiguity well, but its quality depends on domain-matched data and it struggles with long-range syntax, rare languages, and meanings that cannot be recovered from local correspondences.

# References

[[machinetranslation.epub]]
