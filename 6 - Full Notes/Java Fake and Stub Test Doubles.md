2026-10-30 15:57

Status: #baby

Tags: [[Java Diagnostics Testing and Documentation]]

# Java Fake and Stub Test Doubles

A fake is a working but simplified implementation, such as an in-memory repository replacing a database for a test. A stub supplies predetermined responses for selected calls so the unit under test reaches a desired branch without depending on a real collaborator.

Both are test doubles but answer different questions. A fake can support a broader behavioral scenario, while a stub controls inputs to one path. Neither should silently become the proof for integration behavior that only the production database, network, or filesystem can demonstrate.

# References

[[java23forabsolutebeginners_learnthefundamentalsofjavaprogramming.epub]]
