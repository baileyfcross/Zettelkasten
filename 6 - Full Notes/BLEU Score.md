2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# BLEU Score

BLEU, the Bilingual Evaluation Understudy, compares the n-grams in a machine translation with those in one or more human reference translations. It combines modified n-gram precision—commonly through four-word sequences—with a brevity penalty so a system cannot score well merely by producing a few safe words.

A larger corpus-level score generally indicates more reference-like output, making BLEU cheap and useful for repeated experiments. It does not directly measure grammaticality, meaning, discourse coherence, or style, and a valid paraphrase may score poorly. Comparisons are most defensible when the dataset, tokenization, references, and language pair are held constant.

# References

[[machinetranslation.epub]]
