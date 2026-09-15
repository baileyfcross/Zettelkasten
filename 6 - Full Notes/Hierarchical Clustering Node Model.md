2026-09-14 22:06

Status: #baby

Tags: [[C++ Clustering Result Modeling]]

# Hierarchical Clustering Node Model

The hierarchical result model uses an abstract Node with parent, identifier, and level state plus virtual operations for visitor dispatch, child count, and record count. All leaf nodes occupy level zero, while internal nodes represent successively joined or split groups.

This common interface lets clients traverse a nested clustering without branching on storage layout at every step. Parent links and levels make ancestry explicit but must be updated together during tree construction.

# References

[[dataclusteringincplusplus.pdf]]

