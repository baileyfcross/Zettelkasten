2026-09-14 20:21

Status: #baby

Tags: [[Statistical Learning and Validation]]

# Training Error

Training error measures prediction mistakes on the same observations used to fit a model. It describes how closely the learned rule conforms to its [[Training Dataset]] but usually understates error on new data.

A more flexible method can lower training error even after generalization begins to worsen. The source's one-neighbor classifier reaches zero training error by matching every point to itself, providing an extreme example of why training fit cannot select a model alone.

In the book's examples, very strong or perfect training results are treated as a warning rather than proof of success. Validation error reveals whether added complexity is learning transferable structure or merely reproducing the training partition.

# References

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]
