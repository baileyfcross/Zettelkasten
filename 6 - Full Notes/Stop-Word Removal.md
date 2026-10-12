2026-09-16 01:05

Status: #baby

Tags: [[Text Feature Representation]]

# Stop-Word Removal

Stop-word removal deletes very common function words that often contribute grammatical structure but little topic discrimination. Removing articles, determiners, and similar terms can shrink a vocabulary and reduce the number of text features.

The operation is task dependent. Function words may be uninformative for topical retrieval yet useful for authorship, style, or syntax analysis. A stop list should therefore reflect the representation's purpose rather than be applied automatically to every corpus.

Corpus inspection may justify a [[Custom Stop List]] for names, headers, or recurring artifacts not covered by a general language list. Because removing these terms changes every later frequency and model, the exact list belongs with the recorded preprocessing configuration.

# References

[[featureengineeringformachinelearninganddataanalytics.pdf]]

[[textminingandvisualization.pdf]]
