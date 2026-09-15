2026-09-14 21:34

Status: #baby

Tags: [[Interactive and Semi-Supervised Clustering]]

# Cannot-Link Constraint

A cannot-link constraint states that two observations should not share a cluster. It rules out assignments that would violate known distinctions even when the observations are close under the current representation.

Cannot-link information is not generally transitive, and interactions with must-link components can make a requested cluster count infeasible. Constraint checking should identify conflicts rather than silently returning a distorted solution.

# References

[[dataclustering.pdf]]

