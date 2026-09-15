2026-09-14 22:06

Status: #baby

Tags: [[C++ Partitional and Fuzzy Clustering]]

# K-Prototypes Mixed-Type Center

A K-prototypes center contains numeric means for continuous attributes and categorical modes for discrete attributes. The Kprototype class reuses the Kmean lifecycle but overrides center updating so each schema component receives the correct representative.

This inheritance is possible because assignment and iteration structure remain similar. The subclass also relaxes Kmean's numeric-only dataset validation to admit categorical and mixed records.

# References

[[dataclusteringincplusplus.pdf]]

