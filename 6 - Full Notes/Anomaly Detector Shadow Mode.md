2026-10-11 21:02

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Anomaly Detector Shadow Mode

Anomaly detector shadow mode runs a detector on live telemetry without allowing it to page responders, suppress alerts, or trigger remediation. Its predictions and latency are recorded beside the established process so the team can measure precision, recall, alert-to-incident conversion, and missed events under real workload conditions.

The observation period should span representative cycles and changes rather than a convenient quiet window. Promotion occurs only after thresholds and failure behavior are understood; a promising offline score does not establish that the detector will remain useful amid seasonality, deployments, and changing traffic.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
