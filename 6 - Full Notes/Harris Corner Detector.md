2026-09-16 00:47

Status: #baby

Tags: [[Copy-Move and Resampling Forensics]]

# Harris Corner Detector

The Harris corner detector identifies locations where image intensity changes strongly in two directions. Shifting a window around a true corner produces large differences for movements along either axis, unlike an edge, which changes mainly across one direction, or a flat patch, which changes little.

These stable points provide candidate locations for clone matching. The detector reduces the search space but does not determine whether a forgery occurred; descriptors, geometric grouping, and pixel-level verification must follow.

# References

[[fakephotos.epub]]
