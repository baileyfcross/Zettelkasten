2026-10-19 01:48

Status: #baby

Tags: [[Go Control Flow Functions and Errors]]

# Go Blank Identifier

The Go blank identifier `_` accepts a value without creating a usable binding. It lets code discard one position from [[Go Multiple Return Values]] or [[Go Range Iteration]] while still matching the operation's required arity.

It also appears as a blank import alias to request package initialization without using exported names and as an unnamed struct field for layout. Because the value cannot be retrieved, the identifier communicates intentional nonuse rather than a forgotten variable.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
