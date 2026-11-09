2026-11-08 16:45

Status: #baby

Tags: [[Cloud Data Storage Selection and Consistency]]

# Follower Read

A follower read serves data from a nearby replica at a deliberately historical timestamp instead of coordinating with the current leaseholder for the latest state. The bounded staleness allows dashboards, catalogs, and analytic views to reduce cross-region latency when absolute freshness is not required.

The query must make the time tradeoff visible because a successful write may not yet appear in the selected snapshot. Follower reads improve locality and read scale but are inappropriate for a decision that requires the newest value, such as validating a just-updated balance. Consistency requirements therefore belong to the use case, not only to the database configuration.

# References

[[prospringboot4_anauthoritativeguidewithbestpractices.epub]]
