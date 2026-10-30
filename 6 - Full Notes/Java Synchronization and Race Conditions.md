2026-10-30 15:57

Status: #baby

Tags: [[Java Concurrency and Reactive Streams]]

# Java Synchronization and Race Conditions

A race condition occurs when a result depends on unsafely interleaved access to shared mutable state. Java `synchronized` methods and blocks associate exclusive execution and memory visibility with an object's monitor, so related reads and writes can be treated as one protected operation.

Marking a field `volatile` makes updates visible but does not turn a multi-step read-modify-write operation into an atomic action. The safer design is often to reduce shared mutation, give state one owner, use concurrent abstractions, or pass immutable values rather than adding locks around every field.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
