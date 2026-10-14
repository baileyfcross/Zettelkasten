2026-10-08 01:04

Status: #baby

Tags: [[R Software Testing]]

# R Unit Test Reporter

An R unit test reporter controls how a test run presents passes, expectation failures, and unexpected errors. Running a file or directory through the testing framework produces a consolidated result instead of stopping at the first failing expression, which makes repeated execution of a [[Unit Test]] suite practical.

Different reporting modes support different tasks. A compact stream of symbols is useful during a tight repair loop, a summary adds locations and diagnostics for [[Test Failure Localization]], a stop-on-failure mode supports immediate interactive investigation, and a silent structured result supports programmatic analysis. Reporting changes presentation, not the meaning of the tests.

# References

[[testingrcode.pdf]]
