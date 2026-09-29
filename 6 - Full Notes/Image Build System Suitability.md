2026-09-28 04:01

Status: #baby

Tags: [[Image Derivative Workflows]]

# Image Build System Suitability

A prebuilt derivative system fits a small or medium catalog with a manageable set of transformations, relatively infrequent changes, and a need for review before publishing. Its rules can be encoded in scripts and run as part of asset deployment.

It becomes awkward when the master collection or variant matrix changes continuously. Long rebuilds, hardcoded dimensions, and synchronizing every output across servers then favor on-demand generation. See [[Dynamic Image Server Request Pipeline]].

# References

[[highperformanceimages.pdf]]
