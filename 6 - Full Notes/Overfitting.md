2026-09-06 00:13

Status: #baby

Tags: [[Neural Network Training]] · [[Statistical Learning and Validation]]

# Overfitting

Overfitting occurs when a model conforms so closely to its [[Training Dataset]] that it performs poorly on unfamiliar examples. It resembles learning a fixed set of answers by rote without learning the reusable relationship needed to solve new problems.

Additional [[Training Epoch|training epochs]] can continue reducing training error while making generalization worse. Comparing performance against a withheld [[Test Dataset]] reveals this gap and helps determine when more fitting has stopped being useful.

The source illustrates the problem with k-nearest neighbors: using one neighbor classifies every training observation perfectly because each point is its own nearest neighbor, yet it performs poorly on new data. Training fit alone therefore rewards excessive flexibility.

# References

[[algorithms.epub]]

[[dataanalysisforthelifescienceswithr.pdf]]
