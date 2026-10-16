2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# Pregroup Grammar Reduction

Pregroup grammar assigns each word a type in an ordered, noncommutative algebra with distinct left and right adjoints. Concatenating word types represents the grammatical structure of a sentence, and contracting adjacent type-adjoint pairs reduces a well-formed expression to the sentence type $s$.

For “Alice loves Bob,” the nouns receive type $n$ and the transitive verb receives $n^r s n^l$. The full expression $n(n^r s n^l)n$ contracts through $nn^r\leq 1$ and $n^l n\leq 1$, leaving $s$. The two adjoints encode that the verb expects a noun on each particular side.

This reduction is more than a grammatical validity test in [[DisCoCat Compositional Sentence Model]]. Its contraction pattern determines which semantic tensor wires connect and therefore helps define the circuit produced by [[DisCoCat Diagram-to-Circuit Translation]].

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
