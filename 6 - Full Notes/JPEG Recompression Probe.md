2026-09-16 00:47

Status: #baby

Tags: [[JPEG Compression Forensics]]

# JPEG Recompression Probe

A JPEG recompression probe repeatedly saves a test image at candidate quality settings and measures the pixel difference between each result and the original file. A region previously encoded at one of those settings can show an anomalously small or structured difference near the matching quality.

Comparing the difference maps across qualities is the operational basis of [[JPEG Ghost]] analysis. The probe must preserve relevant alignment and encoding conditions, and it should be treated as a test of compression history rather than direct proof of compositing.

# References

[[fakephotos.epub]]
