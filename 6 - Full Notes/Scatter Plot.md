2026-09-06 18:44

Status: #baby

Tags: [[Health Data Visualization]] · [[Exploratory and Robust Data Analysis]] · [[Exploratory Data Visualization in R]]

# Scatter Plot

A scatter plot places paired measurements as points on two quantitative axes. It can reveal direction, curvature, clusters, changing variance, and unusual observations before a correlation or regression coefficient is interpreted.

Color or symbol can encode a grouping variable so analysts can see whether the overall pattern differs across subpopulations. Heavy overplotting, restricted ranges, and influential outliers can all obscure the relationship and should be considered when styling the graph.

In the source's paired-height example, plotting every father-son observation reveals a relationship that the two marginal means and standard deviations omit. The graph provides the context needed to interpret a [[Pearson Correlation Coefficient]] rather than treating the coefficient as a complete description.

The book implements scatter plots in an R grammar-of-graphics workflow, mapping variables to axes and optional color groups. Faceting, labels, and explicit export settings turn the exploratory display into a reproducible analytic artifact.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]
