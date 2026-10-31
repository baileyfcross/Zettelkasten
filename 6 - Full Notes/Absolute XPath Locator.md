2026-10-31 12:52

Status: #baby

Tags: [[Selenium Element Location and DOM]]

# Absolute XPath Locator

An absolute XPath locator describes every step from the document root to a target element and begins with a single slash. It can identify an element precisely when the whole hierarchy is known.

The precision is also its weakness: inserting or rearranging an ancestor can invalidate the entire path. A [[Relative XPath Locator]] based on stable attributes is generally more resilient to ordinary DOM restructuring.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
