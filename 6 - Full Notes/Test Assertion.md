2026-09-27 11:46

Status: #baby

Tags: [[Test-Driven Development and Unit Test Design]] [[Selenium Assertions Exceptions and Test Reliability]]

# Test Assertion

A test assertion compares an observed result with an expected condition and causes the test to fail when that condition is not met. Assertions can examine values, types, exceptions, collections, or interactions according to the behavior under test.

Specific assertions produce useful failure messages and avoid accepting unintended outcomes. The expected condition should express the public behavior rather than restating private implementation steps.


In Selenium tests organized with TestNG, a [[Hard Test Assertion]] stops the current method at the first required failure, while a [[Soft Test Assertion]] records independent failures until [[Soft Assertion Aggregation|`assertAll()`]] reports them together.

# References

[[hands-onsoftwarearchitecturewithc8andnetcore3.pdf]]

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
