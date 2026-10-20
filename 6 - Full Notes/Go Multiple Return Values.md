2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Multiple Return Values

A Go function can return zero, one, or several values in a single call. This supports contracts such as a result paired with an error or a map value paired with a presence indicator without packaging the outputs into an extra object.

Callers receive the results through a matching multiple assignment and can discard an unwanted position with the [[Go Blank Identifier]]. Multiple results make success and expected failure explicit in ordinary control flow, especially in the [[Go Error Value Pattern]].

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
