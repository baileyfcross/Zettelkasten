2026-10-03 22:25

Status: #baby

Tags: [[Platform Technical Debt and Evolution]]

# Platform Technical Debt Weighting

Platform technical debt weighting ranks obligations by their effect rather than treating every imperfection equally. Security or compliance exposures, system-integrity risks, high recurring toil, and constraints on critical delivery paths generally deserve more weight than stable automation that merely needs occasional maintenance.

Weight should combine likelihood, impact, time consumed, affected users, reversibility, and opportunity cost. Regular review is necessary because a low-weight dependency can become urgent after a vulnerability, abandonment, or growth in adoption. The ranking guides investment while preserving an explicit record of debt that remains accepted.

# References

[[platformengineeringforarchitects.pdf]]
