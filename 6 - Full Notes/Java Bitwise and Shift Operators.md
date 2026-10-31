2026-10-30 15:57

Status: #baby

Tags: [[Java Operators and Pattern Matching]]

# Java Bitwise and Shift Operators

Java bitwise `~`, `&`, `|`, and `^` operate on the individual bits of integer values. They can build masks, set or clear flags, and combine binary fields, but their meaning depends on fixed-width two's-complement representation.

`<<` shifts left, `>>` shifts right while preserving the sign bit, and `>>>` shifts right while introducing zeros. Shift counts are masked to the operand width, and overflow bits are discarded. These operators can express multiplication or division by powers of two, but clarity and correctness matter more than replacing ordinary arithmetic reflexively.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
