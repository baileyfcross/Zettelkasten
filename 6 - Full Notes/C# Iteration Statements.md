2026-09-08 21:16

Status: #baby

Tags: [[C Sharp Operators Flow and Conversion]]

# C# Iteration Statements

C# provides `while`, `do`, `for`, and `foreach` statements for repetition. A `while` loop tests before each iteration, a `do` loop runs once before testing, and a `for` loop gathers initialization, condition, and update into one header.

`foreach` obtains an enumerator and repeatedly advances it through a sequence's current items. The iteration variable is not a mechanism for replacing the underlying current item. Choosing a loop should make the stopping condition and source of progress easy to verify.

Control statements refine the path through a loop: `break` leaves it, while `continue` skips the remainder of the current iteration and begins the next test. Because a `do` loop evaluates its condition afterward, it is the deliberate choice when the body must execute at least once.

# References

[[c80andnetcore30moderncross-platformdevelopment.pdf]]
[[introductiontogamedesignprototypinganddevelopment3e.pdf]]

[[programmingincexam70-483mcsdguide.pdf]]
