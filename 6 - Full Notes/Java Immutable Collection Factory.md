2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Immutable Collection Factory

The `List.of`, `Set.of`, and `Map.of` factory methods create compact unmodifiable collections from supplied elements. Structural operations such as adding or removing are unsupported, making the returned value suitable for a fixed configuration or test fixture.

Unmodifiable structure is shallow: if an element is mutable, its internal state can still change. These factories also reject null values and, for sets and maps, duplicate elements or keys. Their contract is therefore stronger than merely wrapping a collection whose original mutable reference is still exposed elsewhere.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
