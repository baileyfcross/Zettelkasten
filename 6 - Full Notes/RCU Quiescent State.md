2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# RCU Quiescent State

An RCU quiescent state is evidence that a CPU or task has passed through a point where it cannot still be inside an older relevant read-side critical section. Context switches, user-mode execution, idle periods, or explicit reporting can provide that evidence depending on the RCU flavor.

Collecting the required quiescent states lets Linux determine that an [[RCU Grace Period]] has elapsed. The concept avoids tracking every individual read lock while still proving that objects removed before the period are no longer reachable by old readers.

# References

[[linuxkernelprogramming_secondedition.pdf]]
