2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Map Collection

A Java `Map<K,V>` associates unique keys with values. Inserting an existing key replaces its prior value, and views expose keys, values, or key-value entries for traversal. A map is not a subtype of `Collection` because its elements are associations rather than single values.

`HashMap` uses key hashing for general lookup, while `TreeMap` orders keys according to natural order or a comparator. Key equality and hash stability are therefore part of the map's correctness, especially when a key object is mutable.

`HashMap` offers expected constant-time basic operations only under effective hash distribution. Collisions create shared buckets, growth can trigger an $O(n)$ redistribution, and a heavily populated bucket may become a red-black tree; ordering, concurrent access, range operations, and null handling can instead point to other map implementations.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[practicaldatastructuresandalgorithmsforjavadevelopers_fromfundamen.epub]]
