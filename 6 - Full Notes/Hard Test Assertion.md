2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Hard Test Assertion

A hard test assertion is a required checkpoint whose failure immediately interrupts the current test and marks it failed. It is appropriate when later steps would be meaningless or misleading without the asserted precondition or outcome.

The immediate stop makes the first blocking failure clear, but prevents collection of later checks in the same method. Noncritical independent observations may instead use a [[Soft Test Assertion]].

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
