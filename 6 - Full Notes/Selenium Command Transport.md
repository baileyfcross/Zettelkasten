2026-10-31 12:52

Status: #baby

Tags: [[Selenium WebDriver and Browser Sessions]]

# Selenium Command Transport

Selenium command transport carries operations from a [[Selenium Client Language Binding]] to a [[Browser Driver]] and returns the result. The book's architecture diagram depicts Selenium commands encoded as JSON and sent over HTTP through the JSON Wire Protocol; its history section also identifies Selenium 4's adoption of the W3C WebDriver standard.

This boundary separates the language-facing test API from browser-specific execution. A test can therefore keep the same high-level operations while changing the driver and browser underneath.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
