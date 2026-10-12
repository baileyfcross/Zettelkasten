2026-09-17 09:48

Status: #baby

Tags: [[Big Data Preprocessing]]

# Minimum Redundancy Maximum Relevance

Minimum redundancy maximum relevance selects features that are strongly related to the target while avoiding variables that repeat information already supplied by selected features. It balances usefulness against overlap rather than scoring each variable in isolation.

The mRMR search can be redesigned for parallel platforms because relevance and redundancy calculations become expensive across many features and records. Parallelism must preserve the criterion while dividing its calculations.

# References

[[frontiersofdatascience.pdf]]
