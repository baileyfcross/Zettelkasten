2026-10-19 01:48

Status: #baby

Tags: [[Go Program Structure and Toolchain]]

# Go Lexical Scope

Go resolves identifiers through nested lexical scopes that include universe, package, file, function, and statement-block regions. An inner declaration can shadow a name from an enclosing scope without changing the outer variable.

Imports are scoped to their source file even though other package declarations are shared across the package. Control constructs can introduce implicit scopes, so a variable declared in an `if` initializer or short declaration may exist only through that statement and its branches.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
