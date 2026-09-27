2026-09-27 00:11

Status: #baby

Tags: [[.NET Synchronization and Thread Coordination]]

# ManualResetEvent

A `ManualResetEvent` acts as a gate: once signaled, it allows all current and later waiters to pass until code explicitly resets it. It is useful for representing a shared condition such as readiness or availability that remains true for a period.

Resetting at the wrong time can strand participants or let them pass under a stale condition. `ManualResetEventSlim` avoids a kernel wait handle on its cheaper paths and is appropriate for short in-process waits.

# References

[[hands-onparallelprogrammingwithc8andnetcore3.pdf]]
