2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# RCU Grace Period

An RCU grace period is an interval long enough for every reader that could have seen an old object before its removal to finish. After the period completes, an updater can reclaim that retired version without invalidating any pre-existing [[RCU Read-Side Critical Section]].

Grace-period completion does not mean all possible readers have stopped; new readers can operate on the newly published version. Linux detects progress through flavor-specific [[RCU Quiescent State]] observations and provides synchronous waits or deferred callbacks for reclamation.

# References

[[linuxkernelprogramming_secondedition.pdf]]
