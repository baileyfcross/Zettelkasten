2026-09-06 22:42

Status: #baby

Tags: [[In-Memory Data Processing]]

# Open Nested Transaction

An open nested transaction can expose its committed effects before the parent transaction finishes. This improves concurrency because other work need not wait for the entire parent.

Early visibility weakens simple rollback: if the parent later aborts, the system may need a compensating action rather than erasing an effect that other transactions have already observed.

# References

[[bigdatamanagementandprocessing.pdf]]
