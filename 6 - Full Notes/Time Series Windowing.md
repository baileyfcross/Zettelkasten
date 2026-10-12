2026-09-15 23:23

Status: #baby

Tags: [[R Time Series Data Structures]]

# Time Series Windowing

Time-series windowing selects observations whose [[Time Index|time indexes]] fall within a specified interval. A window can isolate a season, an event period, or a comparable span without changing the underlying temporal coordinates. With a [[zoo Time Series Object]], the window operation produces another indexed series, so subsequent plotting or [[Time Series Aggregation]] continues to interpret the selected values as observations in time.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
