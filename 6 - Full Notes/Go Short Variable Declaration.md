2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Short Variable Declaration

The Go `:=` form declares block-local variables and initializes them from the expressions on its right. Types are inferred from those values, and a multiple short declaration may reuse existing variables when at least one name is newly declared in the same scope.

This form is unavailable for package-level declarations, where `var` is required. Its compactness is especially useful with [[Go Multiple Return Values]], but an unintended inner declaration can shadow an outer name under [[Go Lexical Scope]].

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
