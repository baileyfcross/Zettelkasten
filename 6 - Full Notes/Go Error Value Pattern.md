2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Error Value Pattern

Go represents expected operation failure with an `error` value, conventionally returned as the last result of a function. A nil error indicates success, while a non-nil value supplies an `Error() string` description and causes callers to follow an explicit failure path.

This keeps recoverable failure in ordinary control flow rather than exception unwinding. Other results generally have meaning only when the error is nil, so callers should test the error before consuming the associated value.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
