2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Go Goroutine Scheduling

The Go runtime scheduler maps runnable goroutines onto operating-system threads and can detach a goroutine when it blocks so another can use the thread. Stacks grow with demand, helping large goroutine populations consume resources in proportion to their actual calls.

`GOMAXPROCS` bounds simultaneous execution of Go code relative to available processors, but scheduling and start order remain nondeterministic. Correct programs coordinate through synchronization and channels rather than depending on observed timing from a particular run.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
