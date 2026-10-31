2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]] · [[Java String Processing and Mutable Text]]

# Java String Formatting and Concatenation

Java can assemble text with the `+` operator, `String.concat`, `StringBuilder`, `String.format`, formatted instance methods, and message-formatting utilities. Concatenation is direct for a few values, while a formatter makes the placement and representation of many values explicit.

The choice affects readability and allocation. Repeated `+` in a loop can generate intermediate Strings, so a builder is more suitable for incremental construction. Locale-sensitive user messages belong with internationalization facilities rather than with a fixed machine-oriented format string.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
