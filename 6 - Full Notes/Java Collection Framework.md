2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Collection Framework

The Java Collection Framework supplies interfaces and implementations for groups of objects. `Collection` branches into list, set, and queue forms, while `Map` models key-value associations outside that inheritance branch. Generic type arguments let the compiler preserve element and key/value types.

Choosing a collection means choosing semantics before implementation: duplicates, ordering, lookup keys, queue discipline, mutability, and concurrency requirements determine the appropriate interface. A concrete class such as `ArrayList`, `HashSet`, or `HashMap` then supplies a particular storage and performance strategy.

Java 21 added sequenced interfaces that express encounter order consistently across collections and maps. [[Java Sequenced Collection]], [[Java Sequenced Set]], and [[Java Sequenced Map]] expose first, last, and reversed views without forcing callers to depend on a particular implementation such as a list or linked map.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
