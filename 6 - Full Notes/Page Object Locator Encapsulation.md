2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# Page Object Locator Encapsulation

Page object locator encapsulation keeps element selectors and browser-specific interaction details inside the page class. Tests depend on the page's behavior-oriented methods rather than IDs, XPath expressions, or CSS structure.

When the UI changes but the user operation remains the same, the locator is updated once in the page object. The benefit is lost if tests reach around the object and manipulate its internal elements directly.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
