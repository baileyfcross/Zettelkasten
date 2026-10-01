2026-09-05 16:28

Status: #baby

Tags: [[Speech and Acoustic Modeling]] · [[Machine Translation Architectures]]

# Statistical Language Model

A statistical language model assigns probabilities to word sequences. During speech recognition, it favors hypotheses that form plausible linguistic continuations even when the acoustic signal alone is ambiguous.

The language score is combined with the [[Acoustic Model]] during [[Speech Recognition Search]]. Traditional recognizers commonly use an [[N-Gram Language Model]], while neural systems can model longer context.

In [[Statistical Machine Translation]], a target-language model ranks candidate translations independently of how their words were obtained from the source. It can prefer “the red car” over permutations of the same words and can favor a less common lexical equivalent when that choice creates a much more probable sentence. Translation quality therefore depends on the joint effect of the translation model and language model, not on picking the highest-probability word correspondence in isolation.

# References

[[aiassistants.epub]]

[[machinetranslation.epub]]
