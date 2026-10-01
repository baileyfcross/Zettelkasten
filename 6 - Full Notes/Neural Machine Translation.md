2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Architectures]]

# Neural Machine Translation

Neural machine translation trains an [[Encoder-Decoder Network]] to represent a source sentence and generate a target sentence as one learned system. Words or subword units enter as dense vectors, internal layers learn contextual structure, and the decoder predicts the translation one unit at a time.

Unlike modular statistical systems, the neural model can optimize its representations end to end and use an [[Attention Mechanism]] to consult relevant source positions during generation. This improves long sentences and reordered language pairs, but demands large corpora and substantial computation. Unknown words, omitted phrases, opaque internal representations, and sensitivity to the training distribution remain practical risks.

# References

[[machinetranslation.epub]]
