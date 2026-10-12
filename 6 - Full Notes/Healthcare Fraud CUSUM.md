2026-09-28 03:19

Status: #baby

Tags: [[Healthcare Fraud Analytics]]

# Healthcare Fraud CUSUM

Healthcare fraud CUSUM uses a cumulative sum statistic to detect small persistent departures from expected provider behavior. Each new observation contributes evidence for or against a shift, and an alarm occurs when accumulated deviation crosses a threshold.

CUSUM can identify gradual change that never produces one extreme claim. Its sensitivity depends on the reference level, expected shift, and decision limit. If the baseline is not stable or is poorly adjusted for seasonality and practice changes, the accumulation can create systematic false alarms.

# References

[[healthcaredataanalytics.pdf]]
