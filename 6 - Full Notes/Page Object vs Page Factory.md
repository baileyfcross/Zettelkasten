2026-10-31 12:52

Status: #baby

Tags: [[Selenium Page Objects and TestNG]]

# Page Object vs Page Factory

The Page Object Model is the design pattern that separates page behavior from test logic; Page Factory is an annotation-based way to initialize elements inside that pattern. Ordinary page objects use explicit locators and `findElement()`, while Page Factory uses `@FindBy` and `initElements`.

They are not mutually exclusive architectures. A project can begin with explicit page objects and adopt Page Factory where its concise declarations improve readability without obscuring dynamic behavior.

# References

[[javatestingwithselenium_acomprehensivesyntaxguideforautomation.epub]]
