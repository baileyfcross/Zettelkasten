2026-10-03 22:25

Status: #baby

Tags: [[Platform Technical Debt and Evolution]]

# Platform Data Retention Debt

Platform data retention debt is the accumulating storage, indexing, performance, security, and governance burden created by keeping data longer or at greater resolution than its value justifies. As the platform changes, old telemetry may also become less comparable and less useful for current decisions.

Every retained dataset should have a consumer, required duration, access model, and deletion or aggregation rule. Rolling detailed observations into coarser periods can preserve long-term trends without preserving every event. Minimization reduces both operating cost and the surface that must be investigated if data is exposed.

# References

[[platformengineeringforarchitects.pdf]]
