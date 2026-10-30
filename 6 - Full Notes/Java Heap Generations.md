2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Heap Generations

A generational Java heap separates newly allocated objects from objects that have survived collection. New objects begin in eden, surviving objects can move between survivor spaces and accumulate age, and sufficiently old objects are promoted to an old or tenured area.

The arrangement exploits the observation that many objects die young, allowing frequent collection to focus on a smaller region. Modern collectors such as G1 implement these roles with flexible regions rather than one fixed contiguous partition, so the logical generations remain while their physical sizes can change.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
