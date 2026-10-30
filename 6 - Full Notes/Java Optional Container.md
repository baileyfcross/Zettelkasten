2026-10-30 15:57

Status: #baby

Tags: [[Java Streams and Functional Processing]]

# Java Optional Container

`Optional<T>` represents either one non-null value or an empty result. Factory methods create an empty optional, wrap a known non-null value, or accept a possibly null input. Stream selection operations use it because a first, minimum, or matching element may not exist.

Callers can transform or filter the contained value and choose defaults through eager `orElse`, lazy `orElseGet`, or exception-producing `orElseThrow`. Optional makes expected absence explicit in a return type; calling `get` without establishing presence merely moves the failure to another operation.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
