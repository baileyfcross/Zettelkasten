2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# Pivot Language Translation

Pivot language translation handles a poorly resourced language pair by translating through a third language with better data, commonly English. A Greek-to-Finnish request, for example, can be decomposed into Greek-to-English and English-to-Finnish systems.

The strategy broadens coverage without requiring a direct parallel corpus, but it compounds errors across both stages. Idioms may be rendered correctly into the pivot and then translated literally, while ambiguity introduced by the pivot can select the wrong target meaning. Heavy reliance on one pivot also reproduces the cultural and technical dominance of that language throughout the system.

# References

[[machinetranslation.epub]]
