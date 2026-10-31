2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# TestNG Annotation Lifecycle

TestNG lifecycle annotations place setup and cleanup at suite, XML-test, class, or method scope. `@BeforeSuite` and `@AfterSuite` surround the suite; corresponding Test, Class, and Method pairs operate at progressively narrower boundaries.

The chosen scope determines what state is shared. Browser setup in `@BeforeMethod` and cleanup in `@AfterMethod` give each test an isolated session, while broader fixtures reduce setup cost but increase coupling.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
