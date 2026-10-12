2026-09-28 03:43

Status: #baby

Tags: [[Recommendation Hardware Acceleration]]

# Collaborative Filtering Training Accelerator

A collaborative filtering training accelerator computes the similarity or average-difference statistics used to build a neighborhood model. The book's FPGA design supports user-based collaborative filtering, item-based collaborative filtering, and SlopeOne through several parallel execution units.

Training is usually offline and consumes more time than prediction. The accelerator therefore focuses on repeated vector intersections, partial statistics, and a [[Pipelined Similarity Reduction]] rather than storing a complete iterative latent-factor model.

# References

[[highperformancecomputingforbigdata_methodologiesandapplications.pdf]]

