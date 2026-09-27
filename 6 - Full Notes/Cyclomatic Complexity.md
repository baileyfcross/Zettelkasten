2026-09-27 11:43

Status: #baby

Tags: [[C Sharp Code Quality Metrics and Static Analysis]]

# Cyclomatic Complexity

Cyclomatic complexity measures the number of independent control-flow paths through a method or program region. Branches and decision points increase the value, indicating how many distinct paths require reasoning and test coverage.

A high value often suggests that a method owns too many decisions and could be decomposed. The metric does not say which paths are important, so refactoring and tests still require domain judgment.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
