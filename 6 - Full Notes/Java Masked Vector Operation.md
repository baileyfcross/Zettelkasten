2026-10-31 22:04

Status: #baby

Tags: [[Java Vector Masks and Data Movement]]

# Java Masked Vector Operation

A Java masked vector operation applies an operator only to lanes selected by a [[Java Vector Mask]]. It lets a single vector instruction represent conditional element updates without executing a scalar branch for every element.

The inactive-lane behavior depends on the API operation: a masked arithmetic update can preserve the receiver's inactive values, while a masked load supplies defined fallback values and a masked store omits inactive addresses. Correct code must therefore treat the mask as part of the operation's semantics rather than as a performance annotation.

# References

[[masteringsimdwithjavavectorapi_unlockingsingle-coreperformancethro.epub]]
