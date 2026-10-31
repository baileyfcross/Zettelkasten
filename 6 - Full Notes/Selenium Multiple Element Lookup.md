2026-10-31 12:52

Status: #baby

Tags: [[Selenium Element Location and DOM]]

# Selenium Multiple Element Lookup

Selenium multiple element lookup uses `findElements()` to return every element matching a locator as a list. The test can iterate through that list to read values, perform repeated actions, or validate a collection.

Unlike a single-element lookup, an empty result can be inspected without immediately relying on a `NoSuchElementException`. The same ID, name, class, tag, link-text, CSS, and XPath strategies can supply the collection locator.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
