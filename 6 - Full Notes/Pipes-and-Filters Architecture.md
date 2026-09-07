2026-09-06 21:16

Status: #baby

Tags: [[Augmented Reality Software Architecture]]

# Pipes-and-Filters Architecture

A pipes-and-filters architecture divides processing into independent filters connected by data-carrying pipes. Each filter transforms its inputs into outputs without needing to own the entire augmented-reality application.

Tracking, calibration, fusion, and rendering stages can be composed and tested in isolation, and a pipe can cross a network boundary in a distributed system. The interfaces must retain timing, coordinate, and type information needed by downstream components.

# References

[[augmentedreality_pearson.pdf]]
