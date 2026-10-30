2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Garbage Collection Eligibility

A Java heap object becomes eligible for garbage collection when no path of strong references from a garbage-collection root can reach it. Eligibility does not mean immediate reclamation; the selected collector decides when to trace or relocate objects and recover their storage.

Setting one variable to null is sufficient only when it removes the last reachable path. Cycles do not keep objects alive by themselves because reachability begins at roots rather than reference counts. Native resources still require deterministic closure even when their wrapper object eventually becomes unreachable.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
