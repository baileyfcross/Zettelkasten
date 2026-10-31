2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Selenium StaleElementReferenceException

Selenium raises `StaleElementReferenceException` when a previously located element no longer refers to the current DOM, commonly after a page reload or dynamic replacement. The stored reference describes an older node even if a similar element is now visible.

A recovery path relocates the element against the current document and, when appropriate, retries the operation. Unbounded retries can hide persistent application or locator defects, so the policy needs a clear limit.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
