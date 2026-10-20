2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Panic and Recover

A Go panic signals an unexpected or catastrophic condition and begins unwinding the current goroutine's call stack while running deferred functions. Ordinary predictable failures should normally use the [[Go Error Value Pattern]] instead.

`recover` can intercept the panic value only when called from a deferred function in that goroutine. An unhandled panic can terminate the program, so goroutine boundaries that must isolate failures need an intentional recovery and reporting policy rather than assuming another goroutine can catch them.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
