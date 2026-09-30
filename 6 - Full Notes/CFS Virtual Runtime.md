2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# CFS Virtual Runtime

CFS virtual runtime is the weighted measure of CPU service used by the [[Completely Fair Scheduler]]. Runtime advances faster for lower-weight tasks and slower for higher-weight tasks, allowing the scheduler to compare how much of each entity's proportional entitlement has been consumed.

Choosing the runnable entity with the smallest virtual runtime approximates fair sharing over time. Newly awakened tasks are placed relative to the runqueue's current minimum so they receive reasonable latency without gaining an unlimited advantage over tasks that remained runnable.

# References

[[linuxkernelprogramming_secondedition.pdf]]
