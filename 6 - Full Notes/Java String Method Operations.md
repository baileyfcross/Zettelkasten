2026-10-31 13:15

Status: #baby

Tags: [[Java String Processing and Mutable Text]]

# Java String Method Operations

Java String methods inspect character sequences through operations such as `length`, `charAt`, `indexOf`, `lastIndexOf`, `startsWith`, and `endsWith`. Index-based methods use zero-based positions and report an invalid character index with an index-out-of-bounds exception.

Transformation methods such as `replace`, `replaceAll`, `replaceFirst`, `toLowerCase`, and `toUpperCase` return new strings because [[Java String Immutability]] prevents changing the receiver. Regular-expression replacements can select matching substrings, while ordinary character replacement changes every matching character in the returned result.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
