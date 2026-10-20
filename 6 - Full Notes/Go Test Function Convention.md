2026-10-19 01:48

Status: #baby

Tags: [[Go Standard Library and Service Development]]

# Go Test Function Convention

A Go unit test is a function whose name begins with `Test` and whose parameter is `*testing.T`, placed in a source file ending in `_test.go`. The `go test` command discovers these functions and constructs the runner without requiring a main function.

Tests commonly compute a result, compare it with the wanted value, and report failure through the testing object. Keeping tests in the same package permits access to unexported names, while an external test package exercises only the public surface.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
