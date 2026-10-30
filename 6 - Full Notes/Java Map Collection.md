2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Map Collection

A Java `Map<K,V>` associates unique keys with values. Inserting an existing key replaces its prior value, and views expose keys, values, or key-value entries for traversal. A map is not a subtype of `Collection` because its elements are associations rather than single values.

`HashMap` uses key hashing for general lookup, while `TreeMap` orders keys according to natural order or a comparator. Key equality and hash stability are therefore part of the map's correctness, especially when a key object is mutable.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
