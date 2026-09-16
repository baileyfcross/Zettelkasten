2026-09-06 18:44

Status: #baby

Tags: [[Health Data Visualization]] · [[Exploratory and Robust Data Analysis]] · [[Exploratory Data Visualization in R]]

# Box Plot

A box plot summarizes a continuous distribution through its median, quartiles, spread, and observations beyond the whiskers. It provides a compact view of center and asymmetry without requiring a choice of histogram bins.

Side-by-side box plots are especially useful for comparing the same outcome across groups. Their compactness can hide multimodality and sample-size differences, so they work best alongside numerical summaries and other distribution plots.

The source defines the box through the 25th, 50th, and 75th percentiles and places whiskers relative to the interquartile range. This design makes the display useful when a skewed distribution causes the mean and standard deviation to give an incomplete summary.

The book places box plots beside [[Violin Plot|violin plots]] for grouped continuous data. The compact quartile summary and the smoothed distribution view answer complementary questions about center, spread, skewness, and multiple modes.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]
