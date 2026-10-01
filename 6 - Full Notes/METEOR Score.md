2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# METEOR Score

METEOR evaluates a translation by aligning content words and the longer matching sequences around them with a reference. It can normalize inflected forms to stems or lemmas and, when language resources permit, match synonyms rather than requiring identical surface forms.

This semantic flexibility can correlate more closely with human judgments than raw n-gram overlap. It also makes the metric harder to reproduce across languages because results depend on tokenizers, stemmers, synonym resources, and configuration choices. METEOR is therefore a richer but less universally convenient companion to the [[BLEU Score]].

# References

[[machinetranslation.epub]]
