2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Context Cancellation

A Go context carries cancellation, deadlines, timeouts, and narrowly scoped request values across API boundaries. Long-running operations accept a context and can select on its `Done` channel to stop when their caller cancels or time expires.

Derived contexts return a cancellation function that should be called to release resources even when work finishes normally. Cancellation is cooperative: each goroutine or I/O operation must observe the context and return rather than being forcibly terminated from outside.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
