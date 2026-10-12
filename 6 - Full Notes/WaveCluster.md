2026-09-14 21:34

Status: #baby

Tags: [[Density and Grid-Based Clustering]]

# WaveCluster

WaveCluster quantizes the feature space and applies a wavelet transform to the resulting grid. The transform suppresses small fluctuations and highlights connected high-density regions at selected scales.

Because wavelets separate signal by scale, the method can find irregular clusters and reduce sensitivity to point-level noise. Grid resolution and the chosen transform scale determine whether nearby regions remain distinct or merge.

# References

[[dataclustering.pdf]]

