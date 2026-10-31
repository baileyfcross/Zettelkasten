2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]] · [[Java System Runtime Services]]

# Java Finalization and Cleaner

Java finalization lets an object's overridden `finalize` method run before reclamation, but it is deprecated because execution is unpredictable and can cause delays, deadlocks, resurrection, and resource leaks. A program cannot depend on finalization for timely release.

Deterministic resources should implement `AutoCloseable` and be used with try-with-resources. `Cleaner` can register a separate cleanup action as a fallback when an object becomes phantom reachable, but its timing is still collector-dependent and the action must not retain the object it is meant to clean.

The later source records JEP 421 marking finalization and the `finalize` methods for removal. Finalization could be disabled during migration, making its lack of a guaranteed execution time—or any guaranteed execution at all—an explicit compatibility concern rather than merely a performance drawback.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
[[java25andbeyond_modernjavamadeeasy.epub]]
[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
