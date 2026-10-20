2026-10-19 01:48

Status: #baby

Tags: [[Go Types Interfaces and Generics]]

# Go Type Assertion

A Go type assertion extracts a value of a stated concrete or interface type from an interface value. The two-result form returns the value plus a Boolean that reports whether the dynamic type satisfied the assertion.

Using the one-result form when the assertion is false causes a panic, so the Boolean form is appropriate when several runtime types are expected. Assertions expose a narrower capability than the interface contract and should not replace a well-designed interface unnecessarily.

# References

[[goforjavaprogrammers_learngooglesgoprogramminglanguage.epub]]
