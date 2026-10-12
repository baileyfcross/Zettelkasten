2026-09-15 23:23

Status: #baby

Tags: [[R Time Series Data Structures]]

# Time Series Missing-Value Handling

Missing-value handling for a [[Time Series]] must respect temporal order. `na.omit` removes incomplete observations, `na.contiguous` keeps the longest uninterrupted run, `na.approx` interpolates between neighboring values, and `na.locf` carries the last observation forward. These operations make different assumptions about the unobserved interval. The choice affects both the apparent pattern and later displays, so an imputed value should not be treated as an actual measurement.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
