2026-09-27 00:11

Status: #baby

Tags: [[.NET Concurrent Collections and Lazy Initialization]]

# Thread-Local Lazy Initialization

Thread-local lazy initialization creates a deferred value separately for each participating thread. It removes contention over one shared instance and suits reusable scratch state that is meaningful only to the current execution thread.

Each initialized thread consumes its own resources, and task code may resume on a different pool thread. The technique should therefore be reserved for genuinely thread-affine state rather than used as a substitute for operation-local values.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
