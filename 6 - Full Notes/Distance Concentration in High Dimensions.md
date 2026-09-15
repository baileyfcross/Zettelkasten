2026-09-14 21:34

Status: #baby

Tags: [[High-Dimensional and Subspace Clustering]]

# Distance Concentration in High Dimensions

Distance concentration occurs when nearest and farthest pairwise distances become increasingly similar as dimensionality grows under common data models. Irrelevant coordinates accumulate variation until proximity has little contrast.

The effect weakens the neighborhood assumptions used by many clusterers. Feature selection, subspace methods, alternative similarity functions, and domain-aware normalization attempt to recover informative contrast rather than trusting raw full-space distance.

Murtagh emphasizes another consequence in some sparse, high-dimensional settings: approximate equality of large distances can make many triples look equilateral or nearly ultrametric. This symmetry can support coarse hierarchical indexing, but it also makes the chosen representation and proximity test crucial. Data piling is a model- and distribution-dependent opportunity, not a blanket cure for weak distance contrast.

# References

[[dataclustering.pdf]]

[[datasciencefoundations_geometry.pdf]]
