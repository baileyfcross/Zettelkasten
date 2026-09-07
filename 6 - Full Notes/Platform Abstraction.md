2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# Platform Abstraction

Platform abstraction presents a stable software interface over differing cameras, trackers, displays, operating systems, and processing hosts. Application components depend on the required capability rather than on one device's command set or data format.

This supports reuse as an AR setup changes and makes simulated or recorded inputs available during development. The abstraction must still expose performance and calibration properties that materially affect real-time registration.

# References

[[augmentedreality_pearson.pdf]]
