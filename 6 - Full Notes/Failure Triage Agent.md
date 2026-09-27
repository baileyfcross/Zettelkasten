2026-09-27 12:11

Status: #baby

Tags: [[DevOps Agent Safety and Autonomy]]

# Failure Triage Agent

A failure triage agent analyzes a captured CI log and returns a structured classification rather than modifying the workflow. A deterministic extractor first selects lines containing common failure markers; the model then identifies a category, severity, likely cause, recommended next step, and confidence.

The design bounds log length, limits the tool list to signal extraction, forbids destructive commands, and validates the returned JSON. The CI job may continue far enough to collect and upload triage artifacts, but it still reports the original test failure rather than allowing analysis to convert a failed build into success.

# References

[[agenticaifordevopsengineers.pdf]]
