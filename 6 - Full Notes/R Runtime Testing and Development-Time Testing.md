2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Runtime Testing and Development-Time Testing

R testing separates two complementary moments of verification. Runtime testing checks assumptions while a user executes code, especially assumptions about inputs and data; development-time testing checks whether the implementation produces the intended results before it reaches users.

A runtime check is usually an [[R Runtime Assertion]] embedded in a function. A development-time check is commonly a [[Unit Test]] that records an example, an expected value or condition, and an [[R testthat Expectation]]. Runtime checks protect the current execution from unsuitable state, whereas development-time tests protect established behavior from defects and later regressions. Programs that analyze many datasets or serve unknown callers benefit from both because interactive inspection no longer covers every case.

# References

[[testingrcode.pdf]]
