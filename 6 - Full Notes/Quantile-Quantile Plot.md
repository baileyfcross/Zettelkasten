2026-09-06 18:44

Status: #baby

Tags: [[Health Data Visualization]] · [[Exploratory and Robust Data Analysis]] · [[R Statistical Testing and Model Validation]] · [[R Statistical Graphics and Export]]

# Quantile-Quantile Plot

A quantile–quantile plot compares the ordered values of a sample with the quantiles expected from a reference distribution, commonly the normal distribution. Points close to the reference line indicate similar distributional shape.

Systematic curvature or departure in the tails suggests that the reference distribution is a poor description. The plot is a diagnostic aid rather than a mechanical pass–fail test, and its interpretation should consider sample size and the intended model.

The source constructs the plot by pairing observed sample percentiles with theoretical normal percentiles. Approximate alignment supports the normal model used by a small-sample t procedure, whereas systematic tail departures warn that the approximation may be unreliable.

R's quantile-quantile workflow draws the theoretical comparison and adds a reference line to make systematic curvature visible. The primer treats this graphical evidence as complementary to a formal normality test and also uses model-specific diagnostic plots when residuals, rather than raw observations, are the target.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[rprimer.pdf]]
