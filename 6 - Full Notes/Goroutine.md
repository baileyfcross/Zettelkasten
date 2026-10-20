2026-10-19 01:48

Status: #baby

Tags: [[Go Concurrency and Coordination]]

# Goroutine

A goroutine is a function execution scheduled concurrently by the Go runtime. Prefixing a function call with `go` launches it without waiting for a returned result, and the runtime multiplexes many goroutines over a smaller set of operating-system threads.

Goroutines begin with comparatively small stacks that can grow and shrink, enabling much larger populations than conventional fixed-stack threads. Their scheduling order is not predictable, and the process ends when the main goroutine returns, so completion and result delivery require explicit coordination.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
