2026-10-19 01:48

Status: #baby

Tags: [[Go Standard Library and Service Development]]

# Go Benchmark Function Convention

A Go benchmark is a `_test.go` function whose name begins with `Benchmark` and whose parameter is `*testing.B`. The testing runner chooses enough repetitions to measure the operation and reports time per operation, with optional allocation and custom metrics.

Setup and cleanup should be excluded from the timed region. The source describes the newer `b.Loop` form as simplifying the repeated body and reducing optimizer and iteration-count distortions, while benchmark execution remains opt-in because it can be expensive.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
