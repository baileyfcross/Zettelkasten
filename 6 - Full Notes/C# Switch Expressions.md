2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Operators Flow and Conversion]]

# C# Switch Expressions

A C# switch expression maps an input value to a result through a sequence of pattern-and-expression arms. It removes the repeated `case`, assignment, and `break` structure of a statement when the purpose of the decision is simply to produce one value.

Arms are considered in order, so specific patterns should precede broad ones. The discard pattern supplies a default result. Because the construct is an expression, it can initialize a variable directly and makes the common output of all branches visible.

A switch expression places the input before `switch` and maps patterns to results with concise arms. The discard pattern `_` supplies the fallback arm, replacing the statement form's explicit `default` label when the goal is to compute a value.

# References

[[hands-onobject-orientedprogrammingwithc.pdf]]

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
