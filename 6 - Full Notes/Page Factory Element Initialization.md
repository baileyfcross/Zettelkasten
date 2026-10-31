2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# Page Factory Element Initialization

Page Factory element initialization calls `PageFactory.initElements(driver, this)` from a page object's constructor. The call connects annotated fields to the supplied driver so later methods can use them as web elements.

Initialization belongs to creation of the page object, while the actual lookup may be deferred through [[Page Factory Lazy Element Lookup]]. The page must still operate within the correct browser and frame context.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
