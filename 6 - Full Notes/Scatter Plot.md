2026-09-06 18:44

Status: #baby

Tags: [[Health Data Visualization]] · [[Exploratory and Robust Data Analysis]] · [[Exploratory Data Visualization in R]] · [[R Statistical Graphics and Export]] · [[R Base Graphics Composition]]

# Scatter Plot

A scatter plot places paired measurements as points on two quantitative axes. It can reveal direction, curvature, clusters, changing variance, and unusual observations before a correlation or regression coefficient is interpreted.

Color or symbol can encode a grouping variable so analysts can see whether the overall pattern differs across subpopulations. Heavy overplotting, restricted ranges, and influential outliers can all obscure the relationship and should be considered when styling the graph.

In the source's paired-height example, plotting every father-son observation reveals a relationship that the two marginal means and standard deviations omit. The graph provides the context needed to interpret a [[Pearson Correlation Coefficient]] rather than treating the coefficient as a complete description.

The book implements scatter plots in an R grammar-of-graphics workflow, mapping variables to axes and optional color groups. Faceting, labels, and explicit export settings turn the exploratory display into a reproducible analytic artifact.

The primer shows the base R construction in which the initial plot establishes axes and symbols and later calls can add lines, labels, or identified points. Formula and vector interfaces describe the same paired relationship, while color, symbol, and size can encode additional variables only if a readable legend explains them.

The student companion uses scatter plots as the starting point for fitting equations to scientific data. It emphasizes looking at the plotted form before choosing a line, quadratic, or nonlinear curve and then drawing the fitted relationship in the same coordinate system for visual diagnosis.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]

[[rstudentcompanion.pdf]]
