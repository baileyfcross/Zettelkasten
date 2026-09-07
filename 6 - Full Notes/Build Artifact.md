2026-09-06 20:52

Status: #baby

Tags: [[Continuous Integration and Delivery]]

# Build Artifact

A build artifact is a versioned output produced by a successful build pipeline for later deployment. It contains the publishable application files rather than requiring the release pipeline to rebuild from an unverified working tree.

The artifact connects one tested source revision to every environment that receives it. Preserving that identity prevents staging and production from accidentally running packages built from different code.

# References

[[aspnetcore3andreact.pdf]]
