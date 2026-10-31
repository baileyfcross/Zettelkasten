2026-10-31 12:52

Status: #baby

Tags: [[Selenium Element Location and DOM]]

# Selenium Name Locator

A Selenium name locator selects an element by its HTML `name` attribute using `By.name`. It is especially common for form controls whose submitted field name is already part of the page contract.

Names are not guaranteed to be unique, so the test must confirm that the chosen value identifies the intended control. When several elements share a name, [[Selenium Multiple Element Lookup]] or a more specific CSS or XPath locator may be appropriate.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
