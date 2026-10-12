2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Lock-Free Synchronization]]

# RCU Read-Side Critical Section

An RCU read-side critical section marks a region in which a reader may dereference RCU-protected objects that an updater has logically removed but not yet reclaimed. The read-side operations are designed to be extremely cheap and do not exclude other readers or an updater publishing a new version.

The reader must follow RCU pointer-access rules and must not retain an unprotected pointer after leaving the section. Whether sleeping is permitted depends on the RCU flavor, so code must use the API whose execution-context guarantees match the path.

# References

[[linuxkernelprogramming_secondedition.pdf]]
