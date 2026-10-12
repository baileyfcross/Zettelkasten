2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# Translation Decoder Search

Translation decoder search chooses a target sentence from a vast set of partial candidates. Each source word or segment may have several translations, some elements may be omitted or inserted, and target word order may change, so exhaustive enumeration quickly becomes impractical.

A decoder incrementally expands promising hypotheses and prunes weak ones according to translation and language-model scores. The best local word choice need not belong to the best sentence: a lower-probability lexical equivalent can produce a much more plausible target sequence. Decoding is therefore the inference stage that turns the probabilities learned by [[Statistical Machine Translation]] into an actual translation.

# References

[[machinetranslation.epub]]
