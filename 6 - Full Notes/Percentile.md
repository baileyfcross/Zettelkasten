2026-09-06 18:44

Status: #baby

Tags: [[Descriptive Health Statistics]]

# Percentile

A percentile is a value below which a specified percentage of ordered observations falls. The 50th percentile is the median, while the 25th and 75th percentiles bound the central half of a distribution.

Percentiles describe position without assuming a normal distribution and help identify plausible ranges or recoding cutpoints. Their sample estimates can repeat when measurements are discrete or capped, so several requested percentiles may share the same observed value.

In observability analysis, percentiles describe tail latency and help identify extreme execution times that an average can hide. SQL functions can either assign each row a percentile rank or return the continuous or discrete value at a requested percentile. The calculation window, partition, interpolation choice, and cost of sorting a large dataset must be recorded because each changes how a latency threshold is interpreted.

# References

[[analyzinghealthdatainrforsasusers.pdf]]
[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
