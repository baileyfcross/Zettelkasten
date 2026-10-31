2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]] · [[Java String Processing and Mutable Text]]

# Java String Pool

The JVM stores interned string values in a pool so equal literals can share one `String` object. A literal therefore commonly reuses an existing pooled instance, whereas explicitly constructing a new String creates a distinct object even when its characters are equal.

Pooling is safe because [[Java String Immutability]] prevents one user from changing shared character content. It also explains why reference comparison may appear to work for some literals yet fail for dynamically constructed strings; content equality must use `equals` rather than relying on pooling.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
