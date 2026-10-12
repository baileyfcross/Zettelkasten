2026-10-11 21:02

Status: #baby

Tags: [[Enterprise RAG and Multi-Agent Applications]]

# Reciprocal Rank Fusion

Reciprocal rank fusion combines several ranked retrieval lists by awarding each document a score based on the reciprocal of its position in each list. A document that appears near the top of both lexical and vector results accumulates more support than one favored by only a single retriever.

The method is useful when search systems produce incomparable raw scores because it operates on rank positions instead. Its constant and candidate depth should still be tested on a curated question set; fusion improves robustness only when the contributing retrievers provide complementary evidence.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
