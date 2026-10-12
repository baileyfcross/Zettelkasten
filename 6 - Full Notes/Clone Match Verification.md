2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]]

# Clone Match Verification

Clone match verification tests whether feature correspondences actually support a duplicated image region. Candidate pairs should agree under a shared transformation, form a spatially meaningful cluster, and yield strong correlation between the transformed source pixels and proposed copy.

This stage rejects accidental descriptor matches and legitimate repeated objects. Blending, compression, and partial occlusion can lower correlation, so verification balances tolerance for post-processing against the risk of accepting ordinary repetition as tampering.

# References

[[fakephotos.epub]]
