2026-09-15 09:21

Status: #baby

Tags: [[Data Science Deployment and Renewal]]

# Churn Label Definition

A churn classifier needs a business definition of what counts as a customer leaving. Explicit contract cancellation may be straightforward to label. In a prepaid service, inactivity could mean departure, temporary nonuse, or a delayed top-up, so a time and balance rule must be chosen.

That rule is then encoded to label historic training cases. A model can only learn the event as operationally defined; changing the threshold changes the target and possibly the apparent performance. Label design is therefore a substantive business and data science decision.

# References

[[datascience_mit.epub]]
