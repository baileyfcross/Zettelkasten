2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Soft Assertion Aggregation

Soft assertion aggregation calls `assertAll()` after a group of soft checks. The call combines every recorded failure into the test result and ensures that a test cannot appear successful merely because execution continued.

Aggregation belongs after the checks whose failures can safely coexist. If a missing prerequisite would invalidate later operations, a [[Hard Test Assertion]] should stop the test before those operations run.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
