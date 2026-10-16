2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# CCG Approximation for Pregroup Parsing

The theoretical DisCoCat pipeline assumes that each sentence can be converted into a pregroup expression, but the study reports no stable pregroup parser available for its experiment. It substitutes a combinatory categorial grammar parser, specifically Lambeq's BobCatParser, as the nearest practical option.

This substitution moves part of the implemented model away from the idealized formal pipeline. The parser still supplies a compositional grammatical structure that Lambeq can turn into a diagram, but any parsing failures, category choices, or reductions inherit the behavior of the CCG system rather than a native pregroup implementation.

The constraint also motivates [[Grammar-Constrained Synthetic Financial Sentiment Data]]: the input sentences must be simple and regular enough for the available parser, not merely meaningful to a human reader.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
