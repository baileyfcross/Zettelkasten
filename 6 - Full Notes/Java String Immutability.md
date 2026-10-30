2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java String Immutability

A Java `String` object cannot change its character sequence after construction. Operations such as concatenation, replacement, case conversion, and trimming return another String rather than modifying the receiver.

Immutability makes pooled strings safe to share and allows stable hashing, but repeated concatenation can create many temporary objects. `StringBuilder` provides mutable accumulation when text is assembled in a loop, and the finished value can then be converted to an immutable String for use as ordinary application data.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
