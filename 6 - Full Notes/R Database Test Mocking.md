2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Database Test Mocking

R database test mocking replaces part of a remote data-access path with controlled local behavior so a test can run without depending on an unreliable network service. The layer chosen for the [[Mock Object]] determines what the test can still prove.

Mocking only the connection preserves most production query code but may still require a local database and remain slow. Mocking a connection wrapper can use packaged data and preserve some query behavior, improving portability at the cost of database-specific fidelity. Mocking the specific query function removes the database and SQL entirely, making downstream analysis fast and isolated while providing no evidence about connection or query correctness. The right boundary follows the behavior under test rather than a desire to replace every dependency.

# References

[[testingrcode.pdf]]
