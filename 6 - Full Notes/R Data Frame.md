2026-09-06 18:44

Status: #baby

Tags: [[Statistical Computing Workflows]] · [[R Statistical Computing and Data Wrangling]] · [[R Data Ingestion and Review]]

# R Data Frame

An R data frame is a rectangular object whose columns represent variables and whose rows represent observations. Different columns may have different classes, while every column must align to the same set of rows.

Data frames are the principal R objects for health-data analysis. Analysts can select columns, subset rows, add recoded variables, pass the object into functions, and create revised copies as checkpoints. This object-centered workflow differs from the implicit row loop of the [[SAS Data Step]].

The life-science workflow in the source imports delimited tables as data frames and then uses dplyr operations to select variables and filter experimental groups. Row and column alignment makes the object a natural interface between raw observations, graphics, and statistical models.

The book treats the data frame as the main interface among imported records, cleaning operations, visualizations, and predictive models. Reviewing its dimensions, names, classes, and sample rows makes the transition from external resource to analytic object explicit.

# References

[[analyzinghealthdatainrforsasusers.pdf]]

[[dataanalysisforthelifescienceswithr.pdf]]

[[essentialsofdatascience.pdf]]
