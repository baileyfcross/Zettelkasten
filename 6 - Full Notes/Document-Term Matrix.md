2026-10-11 12:45

Status: #baby

Tags: [[Text Feature Representation]]

# Document-Term Matrix

A document-term matrix places documents in rows, vocabulary terms in columns, and a count or weight in each cell. It converts a corpus into a rectangular numerical representation that classifiers, clustering algorithms, and topic models can consume.

The matrix depends on earlier choices such as [[Text Tokenization]], case conversion, stemming, stop-word removal, and minimum term frequency. Because most documents use only a small part of a large vocabulary, the result is normally stored as a [[Sparse Text Feature Matrix]] rather than as a dense array.

# References

[[textminingandvisualization.pdf]]
