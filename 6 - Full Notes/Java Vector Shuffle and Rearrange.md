2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Vector Shuffle and Rearrange

A Java vector shuffle describes a lane-index mapping, and `rearrange` applies that mapping to one or two input vectors. Together they express reversal, interleaving, deinterleaving, indexed lane selection, and the permutations required by sorting networks and scans.

Shuffles are horizontal because values cross lane positions. They can be more costly and less uniformly supported than lane-wise arithmetic, so an algorithm should reuse precomputed shuffle descriptions and minimize unnecessary rearrangements. [[Java Vector Zip and Unzip Transposition]] builds structured permutations from this mechanism.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
