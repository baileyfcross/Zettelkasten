2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# DisCoCat Compositional Sentence Model

The distributional compositional categorical model combines two views of meaning: distributional semantics represents words in vector spaces, while grammatical composition specifies how those word meanings combine into a sentence meaning. Category-theoretic structure supplies a common diagrammatic language for the grammatical reductions and the corresponding tensor operations.

A word's grammatical type determines the shape of its semantic map. A noun can be a vector in a noun space $N$, a transitive verb a bilinear map $N\times N\to S$, and an adjective a linear map $N\to N$. Sentence meaning therefore depends on both the learned word representations and the way syntax connects them.

Unlike a recurrent model that must learn grammatical dependencies from examples, DisCoCat inserts an externally parsed grammatical structure before training. [[Pregroup Grammar Reduction]] produces that structure, and [[DisCoCat Diagram-to-Circuit Translation]] converts it into a quantum computation.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
