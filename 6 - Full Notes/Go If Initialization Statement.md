2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go If Initialization Statement

A Go `if` may begin with a simple initialization statement before its Boolean condition. The declared value remains scoped to the condition, the true branch, and an optional else branch.

This pattern keeps a temporary result close to its test, as in assigning an error and immediately comparing it with nil. The limited scope reduces accidental reuse after the condition while also requiring care when a short declaration could shadow an outer variable.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
