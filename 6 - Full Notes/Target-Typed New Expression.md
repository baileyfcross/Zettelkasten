2026-09-26 22:56

Status: #baby

Tags: [[C Sharp Language and Type Fundamentals]]

# Target-Typed New Expression

A target-typed `new` expression omits the constructed type when the surrounding assignment or argument already determines it. For example, `Dictionary<string, int> scores = new();` avoids repeating the declared type.

The feature reduces syntactic duplication without weakening static typing: the compiler still resolves a concrete constructor from the target type. It is clearest when the target is visible and unambiguous near the expression.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

