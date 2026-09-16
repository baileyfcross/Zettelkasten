2026-09-15 23:23

Status: #baby

Tags: [[R Spatiotemporal Data Structures]]

# STFDF Object

An `STFDF` object stores attribute data for a [[Full Space-Time Grid]] defined by spatial features and a time index. With $n$ locations and $m$ times, its data frame follows an $n m$ row ordering in which the spatial index moves faster than the temporal index. A space-wide multivariate time series can be reshaped and vectorized into this order before constructing the object.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
