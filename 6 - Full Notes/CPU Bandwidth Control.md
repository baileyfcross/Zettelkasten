2026-09-30 01:38

Status: #baby

Tags: [[Linux CPU Scheduling and Control Groups]]

# CPU Bandwidth Control

CPU bandwidth control limits how much processor time a control group may consume during a configured period. Once a group exhausts its quota, its runnable work is throttled until bandwidth is replenished, preventing it from monopolizing shared CPUs.

Quota is distinct from a relative CPU weight: weight divides spare capacity under contention, while a quota imposes an upper bound even when cycles are otherwise available. Poorly chosen periods or limits can introduce burstiness and latency for dependent services.

# References

[[linuxkernelprogramming_secondedition.pdf]]
