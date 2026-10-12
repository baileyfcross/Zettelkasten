2026-09-06 00:13

Status: #baby

Tags: [[Matrix and Vector Computation]]

# Sparse Matrix

A sparse matrix is a [[Matrix]] in which most entries are zero. Instead of reserving memory for every position, an implementation can store only the coordinates and values of nonzero entries.

The web's [[Hyperlink Matrix]] is sparse because each page links to only a tiny fraction of all pages. Exploiting that structure makes calculations over a graph containing billions of nodes far more practical in time and storage.

Text matrices have the same shape problem: each document contains only a small subset of a corpus vocabulary. Coordinate formats store row, column, and value triples for nonzero entries, turning a mostly empty [[Document-Term Matrix]] into a practical [[Sparse Text Feature Matrix]].

# References

[[algorithms.epub]]

[[textminingandvisualization.pdf]]
