2026-10-30 15:57

Status: #baby

Tags: [[Java Application Interaction and Internationalization]]

# Java Scanner Input

`java.util.Scanner` reads tokens and lines from an input source and converts text into strings, numbers, booleans, and other supported forms. With `System.in`, it provides a compact way to build an interactive console program.

Token reads leave delimiters in a different state from full-line reads, so mixing `nextInt` with `nextLine` requires deliberate handling of the remaining line separator. Invalid user text can raise an input mismatch, making validation and retry logic part of the interaction rather than an assumption about correct input.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
