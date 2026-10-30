2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Minor Major and Full Collection

A minor collection reclaims the young generation and copies or promotes surviving objects. Because this region is expected to contain many dead short-lived objects, the work can often be frequent and relatively small, though it still includes stop-the-world phases.

Major or old-generation work examines long-lived storage, while a full collection generally covers the entire heap and may compact it. Terminology and exact phases vary by collector. Frequent full collections usually indicate pressure worth investigating rather than a routine operation to request from application code.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
