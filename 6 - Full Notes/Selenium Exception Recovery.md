2026-10-31 12:52

Status: #baby

Tags: [[Selenium Assertions Exceptions and Test Reliability]]

# Selenium Exception Recovery

Selenium exception recovery catches a specific, anticipated failure and applies a defined response such as retrying a transient lookup, skipping an optional element, refreshing a page, or attaching diagnostic evidence. It keeps a known irregularity from terminating the suite without explanation.

Recovery is valid only when the test can still judge its intended behavior. Catching every exception and continuing would turn genuine defects into [[False Positive|false positives]].

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
