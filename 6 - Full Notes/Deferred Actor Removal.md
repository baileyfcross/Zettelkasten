2026-09-20 23:34

Status: #baby

Tags: [[C++ Game Engine Architecture]]

# Deferred Actor Removal

Deferred actor removal marks an actor for deletion during an update but erases it only after the active actor iteration finishes. This prevents iterator invalidation and use-after-free errors when an actor destroys itself or another actor mid-frame.

New actors may likewise be collected in a pending list until the current traversal completes. The world then applies additions and removals at a controlled synchronization point.

# References

[[gameprogrammingincplusplus.pdf]]
