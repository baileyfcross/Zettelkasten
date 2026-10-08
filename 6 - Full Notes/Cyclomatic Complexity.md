2026-09-27 11:43

Status: #baby

Tags: [[C Sharp Code Quality Metrics and Static Analysis]] [[R Software Testing]]

# Cyclomatic Complexity

Cyclomatic complexity measures the number of independent control-flow paths through a method or program region. Branches and decision points increase the value, indicating how many distinct paths require reasoning and test coverage.

A high value often suggests that a method owns too many decisions and could be decomposed. The metric does not say which paths are important, so refactoring and tests still require domain judgment.

In R, conditionals, loops, `switch`, and short-circuit logical operators add independent paths, but dynamic typing and the language's TRUE/FALSE/NA logic make the exact count less definitive than the design signal. Complexity can be reduced by validating a condition early with an [[R Runtime Assertion]], returning immediately for edge cases, and extracting nested logic into smaller functions. The remaining path count gives a rough lower bound on the distinct cases needed for full branch-oriented testing.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[testingrcode.pdf]]
