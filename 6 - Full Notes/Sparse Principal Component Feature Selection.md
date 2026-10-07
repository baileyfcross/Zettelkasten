2026-10-07 00:46

Status: #baby

Tags: [[Spectral Feature Selection Connections and Evaluation]]

# Sparse Principal Component Feature Selection

[[Principal Component Analysis]] can be written as a least-squares problem whose targets encode leading singular directions. Adding sparsity constrains which original variables participate in reconstructing those directions.

An elementwise L1 penalty can make each component loading sparse while still using many different variables across all components. An L2,1 row penalty instead encourages the entire component system to share one small feature subset, making the formulation a closer fit to feature selection rather than merely sparse loading estimation.

# References

[[spectralfeatureselectionfordatamining.pdf]]

