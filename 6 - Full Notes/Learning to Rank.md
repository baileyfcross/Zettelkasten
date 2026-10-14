2026-09-30 21:11

Status: #baby

Tags: [[Social Recommendation and Behavior Modeling]]

# Learning to Rank

Learning to rank fits a scoring function from relative preferences rather than requiring an absolute numeric target or a discrete class. A training pair says that one item should receive a higher score than another; any score values are acceptable when they satisfy the ordering constraints.

Pairwise evidence can be easier to obtain than calibrated ratings. A user who chooses one search result over results displayed above it supplies a preference signal, and a movie viewer may more reliably say which of two films they enjoyed more than assign either an exact number. The learned score then orders future candidates rather than claiming to measure an intrinsic quantity.

For a recommender, this shifts the target from predicting each item's absolute rating to constructing the most useful ordered candidate set. Relative placement can matter more than any one score because users experience the sequence as a choice architecture and usually inspect only its highest-ranked portion.

# References

[[machinelearning_mit.epub]]

[[recommendationengines.epub]]
