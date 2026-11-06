2026-11-06 13:25

Status: #baby

Tags: [[Software Design Principles]]

# Premature Optimization

Premature optimization changes a system to remove a limitation whose existence or importance has not been established. It differs from basic sound design, which chooses suitable structures and avoids already-known inefficiencies without inventing a bottleneck.

Optimization should begin by locating the actual constraint with measurements. Replacing a list, rewriting a loop, or adding a cache has little user-visible value when most request time is spent in a database, network call, or downstream service. The relevant comparison is the expected end-to-end improvement against the added code, memory, synchronization, infrastructure, tests, and maintenance.

An optimization can also outlive the workload that justified it. Requirements and bottlenecks move while special cases and extra components remain, so performance decisions should be reviewed as the system evolves rather than treated as permanent truths.

# References

[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
