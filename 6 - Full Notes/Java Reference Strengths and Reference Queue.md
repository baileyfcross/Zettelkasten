2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Reference Strengths and Reference Queue

A strong reference keeps its object reachable. A soft reference may be cleared in response to memory pressure and can support memory-sensitive caches; a weak reference is cleared more readily after no strong path remains; and a phantom reference supports post-reclamation coordination without exposing the object again.

Soft, weak, and phantom references can be associated with a `ReferenceQueue`. The collector enqueues cleared references so application code can remove stale keys or release related bookkeeping. These types change reachability policy but do not replace deterministic closure of external resources.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
