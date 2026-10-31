2026-10-31 12:52

Status: #baby

Tags: [[Selenium Element Location and DOM]]

# Relative XPath Locator

A relative XPath locator begins with a double slash and finds a matching element without enumerating the complete route from the document root. It can combine element names, attributes, and conditions to identify a target anywhere in the DOM.

Relative paths are usually less brittle than an [[Absolute XPath Locator]] because unrelated ancestor changes do not alter the match. Stability still depends on selecting attributes and relationships that represent a durable page contract.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
