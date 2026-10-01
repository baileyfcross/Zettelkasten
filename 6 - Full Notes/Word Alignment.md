2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# Word Alignment

Word alignment estimates which source and target words express corresponding content inside aligned sentence pairs. Unlike sentence alignment, the relation is rarely one-to-one: a word can map to nothing, to one word, or to a multiword expression, and reordering can make links cross.

Probabilistic methods begin with many possible links and strengthen pairs that repeatedly co-occur across a large corpus. The result is not a perfect linguistic decomposition but a scored bilingual lexicon that supports translation. Its one-directional assumptions can lose many-to-many expressions, which motivates [[Symmetric Word Alignment]] and [[Segment-Based Machine Translation]].

# References

[[machinetranslation.epub]]
