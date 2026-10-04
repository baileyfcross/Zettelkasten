2026-10-03 17:11

Status: #baby

Tags: [[Cloud-Native Reliability and Service Objectives]]

# Error Budget Burn Rate

An error budget burn rate measures how quickly a service is consuming the failure allowance implied by its service-level objective. The budget is commonly expressed as one minus the target, while the burn rate compares actual consumption with the rate that would exhaust it over the reporting window.

A fast burn can trigger action before the objective is formally violated. This makes it more useful for incident response than a retrospective end-of-period result and gives teams a quantitative way to balance risky change against the reliability allowance that remains.

# References

[[observabilityintheai-nativeera.pdf]]
