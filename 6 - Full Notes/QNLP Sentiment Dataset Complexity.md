2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# QNLP Sentiment Dataset Complexity

The finance QNLP benchmark separates sentence complexity into two synthetic datasets of roughly 1,000 examples each. The low-complexity set averages 4.9 words with a vocabulary of 913; the moderate-complexity set averages 18.4 words with a vocabulary of 1,608.

Both datasets are imbalanced toward positive examples. Negative, neutral, and positive proportions are 34%, 18%, and 48% in the low-complexity set and 37%, 17%, and 46% in the moderate set. Accuracy must therefore be interpreted against more than a uniform three-class baseline.

The complexity split changes both linguistic structure and computational demand. QLSTM training slows markedly on the moderate set, while DisCoCat is evaluated only on the low-complexity set after removing neutral examples. These differences are central to [[QLSTM-DisCoCat Benchmark Comparability]].

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
