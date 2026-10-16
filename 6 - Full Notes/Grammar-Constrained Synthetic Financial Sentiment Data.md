2026-10-16 16:25

Status: #baby

Tags: [[Quantum Natural Language Processing for Financial Sentiment]]

# Grammar-Constrained Synthetic Financial Sentiment Data

Grammar-constrained synthetic data generation uses a language model to produce labeled examples that satisfy both an application requirement and a downstream parser's structural limitations. The study prompts ChatGPT for financial or stock-market sentences labeled negative, neutral, or positive, first with a five-word limit and then with a request for more detailed statements.

This approach addresses a specific dataset gap: real financial sentiment corpora available to the authors were not simultaneously small enough for quantum simulation and grammatically regular enough for the DisCoCat parser. It yields two datasets of roughly 1,000 sentences while retaining a common task for QLSTM and DisCoCat experiments.

Generated fluency does not make the corpus equivalent to naturally occurring investor language. Labels, class balance, vocabulary, and grammatical patterns reflect the prompting process, so conclusions should remain tied to [[QNLP Sentiment Dataset Complexity]] and the synthetic distribution.

# References

[[2023 - Applying QNLP to sentiment analysis in finance.pdf]]
