2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# Page Factory Lazy Element Lookup

Page Factory lazy element lookup defers locating an annotated element until code uses the field. A page object can therefore declare many elements without immediately searching the DOM for all of them.

Deferred lookup can avoid unnecessary work, but an invalid locator may fail later in the test and complicate diagnosis. Dynamic attributes can also make a fixed `@FindBy` declaration unsuitable.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
