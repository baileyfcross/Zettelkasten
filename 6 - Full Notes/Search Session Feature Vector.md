2026-10-11 12:45

Status: #baby

Tags: [[Search Log and Web Text Mining]]

# Search Session Feature Vector

A search session feature vector summarizes an estimated session with measures such as query count, average query length, term popularity, term reuse, inter-query interval, and clicks. This representation lets a clustering algorithm compare sessions rather than individual log events.

Features with wide numerical ranges can dominate distance unless they are scaled, while highly correlated measures can count the same behavior several times. The feature set should reflect the behavioral question and be checked for outliers, robots, and recording artifacts.

# References

[[textminingandvisualization.pdf]]
