2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Runtime Assertion

An R runtime assertion checks that an object or execution state satisfies a required condition and responds immediately when it does not. Assertions are especially useful at the start of an [[R Function]], where a clear error can identify an invalid input before downstream calculations turn it into a misleading result.

The response should fit the contract: unrecoverable input can stop execution, while a correctable or noteworthy condition may justify a warning or message. An assertion can be built over an [[R Assertion Predicate]] so the same condition is available both as a logical result and as a fail-fast guard with a diagnostic explanation.

# References

[[testingrcode.pdf]]
