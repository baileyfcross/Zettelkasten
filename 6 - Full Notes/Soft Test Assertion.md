2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Soft Test Assertion

A soft test assertion records a failed condition without immediately stopping the remaining statements in the test. It allows several independent properties of a page or workflow to be checked during one run.

Continuing does not make the failure optional. A [[Soft Assertion Aggregation|final aggregation step]] must report the collected failures and mark the test failed when any check did not pass.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
