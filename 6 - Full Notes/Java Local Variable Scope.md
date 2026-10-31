2026-10-31 13:15

Status: #baby

Tags: [[Java Object Construction and Class Members]]

# Java Local Variable Scope

A Java local variable belongs to the block in which it is declared, including a method body, constructor body, loop, or nested block. Its lifetime begins when execution enters the declaration's scope and ends when that scope is left.

Unlike fields, local variables do not receive automatic default values and must be definitely assigned before use. A narrower block may declare a same-named variable that hides a declaration from an enclosing context, so qualified access or a less ambiguous name may be needed to state which value is intended.

# References

[[learnjavafundamentals_aprimerforjavadevelopmentandprogramming.epub]]
