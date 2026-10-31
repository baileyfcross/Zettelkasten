2026-10-31 12:52

Status: #baby

Tags: [[Selenium Element Location and DOM]]

# Selenium CSS Combinator Locator

A Selenium CSS combinator locator identifies an element through its relationship to another element. A space selects descendants, `>` selects direct children, `+` selects the immediately following sibling, and `~` selects later siblings under the same parent.

Relationship-based selection adds stable context without encoding every ancestor as an absolute path. The chosen relationship should reflect the page's semantic structure rather than incidental markup depth.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
