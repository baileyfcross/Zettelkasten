2026-09-28 03:43

Status: #baby

Tags: [[Neural Network Hardware Acceleration]]

# Neural Network Pipeline Parallelism

Neural network pipeline parallelism overlaps different stages or adjacent layers so several inputs are in flight at once. A downstream stage begins as soon as the upstream stage produces the portion of data it needs.

Throughput is limited by the slowest stage, and dependencies may restrict how many layers can overlap. The book's design alternates inner-product and scalar-product evaluation to weaken the boundary between two fully connected layers.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

