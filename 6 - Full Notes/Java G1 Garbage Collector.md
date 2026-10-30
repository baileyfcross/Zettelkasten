2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java G1 Garbage Collector

The Garbage-First collector divides the heap into equal-sized regions that can take eden, survivor, or old roles. After concurrent marking identifies live data, G1 prioritizes regions expected to yield substantial free space and evacuates survivors, compacting as it reclaims.

G1 combines concurrent phases with parallel stop-the-world phases and uses a pause prediction model to choose how much work to include in a collection set. Its flexible regional layout replaces fixed generation sizes and has been the default HotSpot collector since Java 9.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
