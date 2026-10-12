2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Algorithm Framework]]

# Fetch Results Hook

fetchResults is a protected pure virtual const operation that converts internal working state into the public Results object. It transfers memberships and inserts method-specific structures or diagnostics such as partitions, hierarchies, error, likelihood, and iteration count.

Keeping publication separate from computation lets internal representations differ from the external contract. It also ensures stale output is cleared immediately before the completed state is exposed.

# References

[[dataclusteringincplusplus.pdf]]

