2026-10-30 15:57

Status: #baby

Tags: [[Java Values Strings and Core Types]]

# Java Stack and Heap Memory

During Java execution, each thread uses stack frames for active method calls, including primitive local values and object references. Objects and arrays are allocated in heap memory, where they can outlive the method that created them as long as a reachable reference remains.

The distinction explains lifetime and access rather than a promise about every implementation detail. Stack frames are removed as calls return, while heap objects are reclaimed by [[Garbage Collection]]. JVM options such as `-Xms` and `-Xmx` configure initial and maximum heap capacity.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
