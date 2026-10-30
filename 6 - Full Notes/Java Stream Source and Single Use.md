2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Stream Source and Single Use

A Java stream can originate from a collection, array, file, generated values, a builder, or another sequence-producing API. The stream is a view of a traversal process rather than a container that owns the elements.

After a terminal operation begins or completes, that stream instance cannot be reused; another stream must be obtained from the source. This one-shot rule lets the implementation fuse and consume operations without preserving a replayable result. Returning an empty stream is preferable to returning null when a method has no elements to supply.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
