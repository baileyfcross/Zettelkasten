2026-10-11 21:02

Status: #baby

Tags: [[AIOps Incident Intelligence]]

# Alert-to-Incident Ratio

The alert-to-incident ratio compares the number of alerts emitted with the number that correspond to actionable operational incidents. A high ratio can indicate duplicate signals, thresholds that react to harmless variation, or models that detect statistical novelty without operational significance.

The measure should be segmented by service, detector, severity, and time period and interpreted with recall. Reducing alerts is not an improvement if important incidents disappear with them; the aim is fewer interruptions per meaningful event while preserving detection of user-impacting failures.

# References

[[ultimateaiguideforlinuxengineers.pdf]]
