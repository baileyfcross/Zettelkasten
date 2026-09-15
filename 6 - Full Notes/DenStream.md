2026-09-14 21:34

Status: #baby

Tags: [[Stream and Big Data Clustering]]

# DenStream

DenStream maintains fading microclusters for evolving data and applies a density-based offline procedure to their current summaries. Potential core microclusters represent stable dense regions, while outlier microclusters track sparse candidates that may grow or disappear.

Exponential decay reduces the influence of old observations and enables adaptation to concept drift. Decay rate and density thresholds determine how quickly genuine new clusters emerge and how long inactive structure persists.

# References

[[dataclustering.pdf]]

