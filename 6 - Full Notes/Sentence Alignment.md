2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# Sentence Alignment

Sentence alignment identifies which sentences in two translated documents correspond. Most mappings are one-to-one, but a translator may split, merge, insert, or omit material, so an aligner must also consider one-to-many and empty correspondences.

Length-based methods exploit the tendency of a long source sentence to have a long translation and use global optimization to avoid cascading errors. Lexical methods add anchors such as cognates, names, numbers, typography, and document structure. Combining these cues creates “islands of confidence” from which the remaining gaps can be aligned, producing the [[Parallel Corpus]] needed for later word- and segment-level learning.

# References

[[machinetranslation.epub]]
