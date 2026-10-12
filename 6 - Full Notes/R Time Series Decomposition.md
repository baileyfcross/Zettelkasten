2026-10-04 22:20

Status: #baby

Tags: [[R Regression and Longitudinal Modeling]]

# R Time Series Decomposition

R time series decomposition separates an observed series into trend, seasonal, and residual components. An additive decomposition treats seasonal amplitude as roughly constant, whereas multiplicative behavior can be approached through a transformation when variation grows with the series level.

The frequency and time indexing define the seasonal cycle, so an incorrectly constructed time-series object produces misleading components. The residual component should be inspected for remaining structure rather than assumed to be noise.

# References

[[rprimer.pdf]]
