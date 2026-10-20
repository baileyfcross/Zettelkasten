2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Expressionless Switch

A Go switch can omit its selector expression, making each case an arbitrary Boolean condition evaluated in order. The first true case runs, with an optional default when no condition matches.

This form provides a flatter alternative to a long `if` and `else if` chain. Each case has its own implicit block, and execution normally stops after that branch rather than continuing into later cases.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
