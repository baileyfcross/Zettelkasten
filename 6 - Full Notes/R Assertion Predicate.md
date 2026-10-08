2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Assertion Predicate

An R assertion predicate evaluates a property and returns a logical result that an [[R Runtime Assertion]] can enforce. A scalar predicate answers one question about the whole object; a vector predicate returns one result per element so failures can retain their positions and causes.

Separating the predicate from the assertion preserves flexibility. Code can branch or repair an input after inspecting the predicate, while an assertion can require that all or any elements pass and choose the severity of failure. Attaching a cause to false results also produces more useful diagnostics than a bare logical value.

# References

[[testingrcode.pdf]]
