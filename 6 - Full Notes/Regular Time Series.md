2026-09-15 23:23

Status: #baby

Tags: [[R Time Series Data Structures]]

# Regular Time Series

A regular time series has observations separated by a constant sampling interval, such as hourly, daily, monthly, or quarterly measurements. Regularity supports predictable alignment and [[Time Series Aggregation]], but it does not guarantee complete data because scheduled observations may still be missing. Calendar-aware indexes such as [[yearmon Time Index]] and [[yearqtr Time Index]] represent common regular periods without pretending that every month or quarter has the same number of days.

# References

[[displayingtimeseriesspatialandspace-timedatawithr2e.pdf]]
