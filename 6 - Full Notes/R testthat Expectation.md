2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R testthat Expectation

A testthat expectation states one observable condition that an R test requires. It can compare an actual value with an expected value, require a particular error, warning, message, or printed output, check an object's type or class, or assert that execution remains silent.

The expectation should be specific enough that the wrong failure cannot accidentally pass. For example, a test of an error should match its message, and a test of a warning-producing calculation should check both the warning and the returned result. Several focused expectations can describe a [[Unit Test]] while keeping a failure easy to interpret through [[Test Failure Localization]].

# References

[[testingrcode.pdf]]
