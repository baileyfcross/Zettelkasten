2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Defer Statement

A Go defer statement schedules a function call to run when the surrounding function returns, whether that return is explicit, reaches the function end, or occurs during panic unwinding. Deferred calls execute in last-in, first-out order.

The pattern keeps cleanup near successful resource acquisition, such as deferring a file close or mutex unlock. Arguments to the deferred call are evaluated when defer is encountered, while a deferred closure may observe or modify captured named results later.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
