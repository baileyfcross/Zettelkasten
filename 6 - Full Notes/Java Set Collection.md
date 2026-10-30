2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Set Collection

A Java `Set<E>` models a collection without duplicate elements according to its equality rule. `HashSet` uses hashing and does not promise sorted order, while `TreeSet` maintains an order through natural comparison or a supplied comparator.

Correct behavior depends on the element contracts. A hash-based set expects equal objects to have equal hash codes, and mutating fields used by equality after insertion can make an element difficult to find. A sorted set expects comparison to define a stable ordering compatible with the intended notion of duplication.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
