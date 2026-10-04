2026-10-04 08:37

Status: #baby

Tags: [[Container Registry Distribution and Trust]]

# Container Registry Garbage Collection

Container registry garbage collection removes blob objects that are no longer referenced by any retained manifest. Deleting a tag or manifest can make content eligible, but the registry's storage does not necessarily reclaim that space until the separate collection process runs.

A dry run should identify candidates before deletion because an unreferenced layer might otherwise have been reused by a future image and will need to be uploaded again. Garbage collection belongs with retention and deletion policy: it is storage reclamation after reference analysis, not a substitute for deciding which images the registry should preserve.

# References

[[podmanfordevopssecondedition.pdf]]
