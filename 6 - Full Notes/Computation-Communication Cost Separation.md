2026-10-07 00:46

Status: #baby

Tags: [[Parallel Spectral Feature Selection]]

# Computation-Communication Cost Separation

Distributed algorithm analysis should account for arithmetic work and network transfer separately. A single transmitted value can cost far more than one local operation, so a complexity expression that combines them into one undifferentiated count can predict scaling poorly.

For parallel feature selection, local matrix products may fall roughly in proportion to worker count while reductions grow with message size and a communication tree. Speedup approaches linear only while the decreasing local computation remains larger than aggregation, synchronization, and coordinator work.

# References

[[spectralfeatureselectionfordatamining.pdf]]

