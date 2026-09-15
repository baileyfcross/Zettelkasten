2026-09-15 10:24

Status: #baby

Tags: [[Scalable Hierarchical Search]]

# Random Projection Hashing

Random projection maps a high-dimensional vector onto one or a few lower-dimensional axes. The projected value can then be quantized into a prefix bin, making projection plus longest-common-prefix matching a similarity-oriented hashing method.

Nearby vectors may land in the same bin, allowing candidate matches to be found without comparing every original pair. Projection and quantization can also cause collisions or separate genuine neighbors, so the book tests stability and compares resulting groups with other methods. The hash is an approximate search aid, not an exact equality test on the original vectors.

# References

[[datasciencefoundations_geometry.pdf]]
