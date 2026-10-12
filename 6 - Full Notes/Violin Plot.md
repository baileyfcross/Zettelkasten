2026-09-16 00:09

Status: #baby

Tags: [[Exploratory Data Visualization in R]] · [[R Statistical Graphics and Export]]

# Violin Plot

A violin plot mirrors a smoothed density estimate around a categorical position to show the shape of a continuous distribution. It can reveal skewness or multiple modes hidden by a [[Box Plot]].

Its width represents estimated density rather than sample size unless explicitly scaled, so the bandwidth and accompanying summaries matter.

The primer constructs the mirrored density and places it on a categorical axis, optionally adding a box-plot summary inside the shape. That combination shows both distribution form and robust location, but the smoothed boundary should not be read as observed data beyond the sample range.

# References

[[essentialsofdatascience.pdf]]

[[rprimer.pdf]]
