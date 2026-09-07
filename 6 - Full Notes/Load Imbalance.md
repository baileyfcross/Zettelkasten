2026-09-06 22:42

Status: #baby

Tags: [[Hardware Acceleration for Big Data]]

# Load Imbalance

Load imbalance occurs when parallel workers receive unequal amounts of useful work and some become idle while others remain busy. In graph processing, a few high-degree vertices can dominate the edges assigned to one partition.

Dynamic work queues, finer partitions, work stealing, and degree-aware distribution can improve balance, but each adds coordination or data-movement cost.

# References

[[bigdatamanagementandprocessing.pdf]]
