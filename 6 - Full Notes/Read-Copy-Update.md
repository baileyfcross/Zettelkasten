2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# Read-Copy-Update

Read-copy-update is a synchronization technique optimized for data that is read far more often than it is changed. Readers enter an inexpensive [[RCU Read-Side Critical Section]] and follow published pointers, while an updater builds a new version and atomically publishes it instead of modifying reader-visible structure in place.

The updater postpones reclamation of the old version until an [[RCU Grace Period]] confirms that pre-existing readers are finished. RCU separates visibility, exclusion among writers, and object lifetime, so writers may still need a conventional lock to serialize their own changes.

# References

[[linuxkernelprogramming_secondedition.pdf]]
