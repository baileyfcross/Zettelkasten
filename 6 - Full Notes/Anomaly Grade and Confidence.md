2026-11-06 12:32

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Anomaly Grade and Confidence

An anomaly grade expresses how unusual an observed data point or bucket is relative to the detector's learned behavior. Anomaly confidence expresses whether the model has observed enough representative data to trust that grade. They answer different questions: a severe-looking deviation can still have low confidence when the detector is new or its history is sparse.

Triggers should therefore consider both values together and preserve the entity, category, time bucket, and comparison period used to produce them. Detector interval also matters: a short interval responds quickly but may classify ordinary fluctuations as anomalies, while a long interval smooths noise at the cost of detection latency.

Confidence is not the same as model accuracy and an anomaly is not a root cause. [[Anomaly Detection Scope]] determines what was evaluated, while correlated traces, changes, dependencies, and other evidence are still needed before the result becomes a defensible incident explanation.

# References

[[observabilityforlegacysystems_methodsandsolutionswithopentelemetry.epub]]
