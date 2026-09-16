2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# Double Quantization Artifact

A double quantization artifact is the periodic over- and under-population of transform-coefficient values produced by rounding at one step size and then at another. Some values from the first quantizer map disproportionately into the bins of the second, leaving a comb-like statistical pattern.

The pattern is evidence of two incompatible JPEG quantization histories and can sometimes be localized to edited regions. Its visibility depends on coefficient frequency, image content, alignment, and the relationship between the two tables.

# References

[[fakephotos.epub]]
