2026-09-30 21:41

Status: #baby

Tags: [[Machine Translation Data Evaluation and Practice]]

# Symmetric Word Alignment

Symmetric word alignment runs an aligner in both translation directions and reconciles the two results. Links supported from source to target and from target to source form a high-precision intersection that avoids the one-to-many bias of a single directional model.

The intersection alone has low recall because many plausible links survive in only one direction. Practical systems therefore expand from the shared links into neighboring alignments using heuristics. This turns reliable correspondences into islands of confidence and makes it possible to extract many-to-many translation segments, at the cost of extra computation and still greater data demands.

# References

[[machinetranslation.epub]]
