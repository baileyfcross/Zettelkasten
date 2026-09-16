2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]]

# Clone Detection

Clone detection finds duplicated regions that may indicate a [[Copy-Move Image Forgery]]. Exhaustively comparing every possible patch is computationally impractical, so a detector first identifies distinctive locations, represents their neighborhoods compactly, and retrieves similar candidates.

Candidate pairs are grouped by a consistent translation, rotation, or scale and then checked against the underlying pixels. Verification is crucial because windows, bricks, foliage, and other repeated scene structures can generate legitimate matches.

# References

[[fakephotos.epub]]
