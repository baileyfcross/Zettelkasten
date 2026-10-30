2026-10-30 15:57

Status: #baby

Tags: [[Java Garbage Collection and Memory Management]]

# Java Garbage Collector Selection and Logging

HotSpot VM options select a collector and expose its configuration and events. Collector-specific `-XX` flags choose implementations, while unified logging options and verbose GC output report the selected collector, pauses, regions, generations, heap occupancy, and exit statistics.

Printing final flags reveals the effective configuration after ergonomic defaults are applied. Logging is evidence for a tuning decision, not the decision itself: pause distributions, allocation rates, live-set size, and application throughput must be related to the workload before changing heap or collector parameters.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
