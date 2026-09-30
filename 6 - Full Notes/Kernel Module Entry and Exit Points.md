2026-09-30 01:38

Status: #baby

Tags: [[Linux Kernel Module Development]]

# Kernel Module Entry and Exit Points

A loadable module registers an initialization function that runs when the module is inserted and a cleanup function that runs before it is removed. The initialization path acquires resources and returns zero for success or a negative kernel error code for failure.

Cleanup reverses every successful acquisition in a safe order. Code or data marked for initialization can be discarded after successful setup, while a failed initializer must leave no live resource that assumes the module remains present.

# References

[[linuxkernelprogramming_secondedition.pdf]]
