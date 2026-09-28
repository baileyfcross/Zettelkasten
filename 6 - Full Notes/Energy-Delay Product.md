2026-09-06 22:42

Status: #baby

Tags: [[Parallel Neural Network Training]]

# Energy-Delay Product

Energy-delay product multiplies the energy consumed by the time required to finish a workload. It penalizes a configuration that saves energy only by becoming extremely slow and one that finishes quickly only by using disproportionate energy.

The metric provides a single comparison for processor count and voltage-frequency choices, although different applications may value delay or energy more strongly than the equal product implies.

It also evaluates memory architecture. A hybrid last-level cache can reduce energy through low-leakage STT-RAM yet increase delay through slow writes; access-aware placement and bank partitioning improve the product only when their energy savings and latency effects are measured together.

# References

[[bigdatamanagementandprocessing.pdf]]

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]
