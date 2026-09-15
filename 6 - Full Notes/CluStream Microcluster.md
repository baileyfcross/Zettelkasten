2026-09-14 21:34

Status: #baby

Tags: [[Stream and Big Data Clustering]]

# CluStream Microcluster

A CluStream microcluster is a compact statistical summary of nearby stream observations. It records sufficient information such as counts, linear and squared sums, and temporal statistics so that centroids, radii, and time properties can be recovered without storing every point.

Online processing updates or creates microclusters, while an offline phase groups snapshots into larger clusters for a chosen time horizon. The separation lets users analyze historical periods after the raw stream has passed.

# References

[[dataclustering.pdf]]

