2026-10-31 12:52

Status: #baby

Tags: [[Selenium Element Location and DOM]]

# Selenium Link Text Locator

A Selenium link-text locator selects an anchor by its visible text. `By.linkText` requires the exact displayed text, while `By.partialLinkText` matches a stable substring when the full label is long or variable.

Visible-text locators make a test readable but are language-dependent and fragile when copy changes. A stable [[Selenium ID Locator|ID]] or data attribute is preferable when a multilingual interface must use one locator across translations.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
