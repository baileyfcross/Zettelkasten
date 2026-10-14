2026-09-06 18:44

Status: #baby

Tags: [[Health Data Visualization]] · [[Exploratory and Robust Data Analysis]] · [[Exploratory Data Visualization in R]] · [[R Statistical Graphics and Export]] · [[R Base Graphics Composition]]

# Box Plot

A box plot summarizes a continuous distribution through its median, quartiles, spread, and observations beyond the whiskers. It provides a compact view of center and asymmetry without requiring a choice of histogram bins.

Side-by-side box plots are especially useful for comparing the same outcome across groups. Their compactness can hide multimodality and sample-size differences, so they work best alongside numerical summaries and other distribution plots.

The source defines the box through the 25th, 50th, and 75th percentiles and places whiskers relative to the interquartile range. This design makes the display useful when a skewed distribution causes the mean and standard deviation to give an incomplete summary.

The book places box plots beside [[Violin Plot|violin plots]] for grouped continuous data. The compact quartile summary and the smoothed distribution view answer complementary questions about center, spread, skewness, and multiple modes.

The primer uses R's formula interface for parallel group box plots and shows that orientation and whisker range are configurable. Extending whiskers to the observed minimum and maximum changes the conventional outlier display, so that option should be stated rather than mistaken for a standard modified box plot.

The student companion uses single and side-by-side box plots to move from one-variable distribution review to group comparison. The shared scale lets medians and spreads be compared directly, while the compact display still needs the sample context supplied by points or numerical summaries.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]

[[rstudentcompanion.pdf]]
