2026-09-30 00:59

Status: #baby

Tags: [[Digital Image Representation and Quality]]

# SVD Image Compression

SVD image compression treats a grayscale image as a matrix and replaces its full singular value expansion with only the leading terms. Large singular values carry the dominant patterns, while discarded smaller terms contribute less to the reconstruction.

A rank-$r$ approximation stores $r(m+n+1)$ scalar values instead of all $mn$ pixels. Raising $r$ improves visual fidelity at the cost of storage, making the method an explicit compression-quality tradeoff based on [[Singular Value Decomposition]].

# References

[[linearalgebra.pdf]]
