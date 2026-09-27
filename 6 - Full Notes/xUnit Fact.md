2026-09-27 11:46

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]]

# xUnit Fact

An xUnit fact is a parameterless test case representing one invariant behavior. A method marked with `Fact` is discovered by the test runner and passes or fails according to its assertions and any unhandled exception.

A fact should communicate one coherent expectation and arrange only the state relevant to it. Several unrelated assertions in one method make a failure less precise and the test more expensive to understand.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]
