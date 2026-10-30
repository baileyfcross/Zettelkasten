2026-10-30 15:57

Status: #baby

Tags: [[Java Collections and Date-Time]]

# Java Date-Time Formatting and Parsing

`DateTimeFormatter` converts `java.time` values to text and parses text according to predefined or custom patterns. The formatter is immutable and can be reused safely, unlike older mutable formatting classes.

Formatting cannot supply information the value does not contain: a local date has no time or zone to print, and parsing zone-sensitive text requires a compatible temporal type. A pattern is a data contract, so localized user display and stable machine interchange should use deliberately different formatters when their requirements differ.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
