2026-09-15 10:16

Status: #baby

Tags: [[Ultrametric Hierarchy and Information]]

# p-Adic Dendrogram Encoding

The book encodes a leaf's root-to-terminal route by placing signed branch labels at powers of a chosen base. Coefficients are -1, 0, or +1, with nonzero terms recording the nodes along that route. The resulting code is a compact numeric representation of a ranked binary dendrogram.

Using a base of at least 3 avoids ambiguous ordinary-integer equivalents for these signed coefficients, and the tree can be reconstructed from the unique codes. Exchanging left and right branch labels changes individual codes while preserving the underlying cluster nesting.

# References

[[datasciencefoundations_geometry.pdf]]
