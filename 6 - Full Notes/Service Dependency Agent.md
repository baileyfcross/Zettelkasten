2026-09-30 17:53

Status: #baby

Tags: [[LLM-Assisted Software Operations]]

# Service Dependency Agent

A service dependency agent identifies the direct and indirect services related to an alerted node by querying topology and dependency data for the incident time. It narrows root-cause investigation beyond the component where a symptom first appeared.

Its output should distinguish observed edges from inferred relationships and preserve direction and timestamps. Dependency evidence is passed to a [[Fault Probability Agent]] alongside logs, metrics, and recent changes rather than treated as proof by itself.

# References

[[llmsformodernsoftwaredeliveryanddevops.pdf]]
