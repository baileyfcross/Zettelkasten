2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Local Date-Time API

The `java.time` API separates a calendar date, a wall-clock time, and their combination into `LocalDate`, `LocalTime`, and `LocalDateTime`. These immutable values do not contain a time zone, so they model information such as a birthday or local appointment rather than a globally unique moment.

Factory and arithmetic methods return new values instead of mutating the receiver. Clear type separation replaces much of the ambiguity and thread-safety difficulty of older `Date`, `Calendar`, and `SimpleDateFormat` usage.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
