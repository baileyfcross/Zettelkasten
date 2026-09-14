2026-09-14 00:20

Status: #baby

Tags: [[Blender Library and Kernel Internals]]

# Blender blenlib Module

`blenlib` is Blender's broad utility module. It provides data structures, linked lists, maps, sets, hashing, memory pools, file and path helpers, threading, timers, byte swapping, geometry algorithms, noise, random values, and mathematical operations used throughout the codebase.

Its services are generally accessed through the [[Blender BLI API]]. Although many utilities are conceptually reusable outside Blender, the module still has meaningful dependencies on the surrounding repository. This distinguishes it from the more application-specific [[Blender blenkernel Module]].

# References

[[coreblenderdevelopment.pdf]]

